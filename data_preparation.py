"""
================================================================================
DATA PREPARATION FOR TABLEAU DASHBOARD
NYC Flight Weather Analysis
================================================================================

This script prepares the nycflights13 weather data for visualization in Tableau.

Steps:
1. Extract compressed data
2. Clean missing values
3. Convert units to metric
4. Aggregate by day and month
5. Export for Tableau

Author: Victor Prefa
Institution: Deakin University
Course: MSc Data Science & Business Analytics

================================================================================
"""

import numpy as np
import pandas as pd
import gzip
import shutil
from collections import defaultdict

# =============================================================================
# CONSTANTS
# =============================================================================

MPH_TO_MS = 0.44704  # Conversion factor: mph to m/s
AIRPORTS = ['EWR', 'JFK', 'LGA']


# =============================================================================
# DATA EXTRACTION
# =============================================================================

def extract_gzip_file(input_path: str, output_path: str) -> None:
    """Extract a gzip compressed file."""
    with gzip.open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"✓ Extracted {input_path} to {output_path}")


# =============================================================================
# DATA LOADING & CLEANING
# =============================================================================

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Load weather data and perform initial cleaning.
    
    Args:
        filepath: Path to CSV file
        
    Returns:
        Cleaned DataFrame
    """
    # Load data
    df = pd.read_csv(filepath)
    
    # Filter valid airports
    df = df[df['origin'].isin(AIRPORTS)]
    
    # Remove rows with missing wind speed
    df = df.dropna(subset=['wind_speed'])
    
    # Convert wind speed to m/s
    df['wind_speed_ms'] = df['wind_speed'] * MPH_TO_MS
    
    print(f"✓ Loaded {len(df):,} observations")
    
    return df


# =============================================================================
# AGGREGATION FUNCTIONS
# =============================================================================

def calculate_daily_means(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily mean wind speeds.
    
    Args:
        df: Weather DataFrame
        
    Returns:
        Daily aggregated DataFrame
    """
    # Create date column
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    
    # Group by date and origin
    daily = df.groupby(['date', 'origin'])['wind_speed_ms'].mean().reset_index()
    daily.columns = ['Date', 'Airport', 'Wind_Speed_ms']
    
    return daily


def calculate_monthly_means(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate monthly mean wind speeds by airport.
    
    Args:
        df: Weather DataFrame
        
    Returns:
        Monthly aggregated DataFrame
    """
    monthly = df.groupby(['month', 'origin'])['wind_speed_ms'].mean().reset_index()
    monthly.columns = ['Month', 'Airport', 'Wind_Speed_ms']
    
    # Pivot for Tableau
    monthly_pivot = monthly.pivot(index='Month', columns='Airport', values='Wind_Speed_ms')
    monthly_pivot = monthly_pivot.reset_index()
    
    return monthly_pivot


def find_top_windiest_days(df: pd.DataFrame, airport: str = 'LGA', 
                           top_n: int = 20) -> pd.DataFrame:
    """
    Find the top windiest days for a specific airport.
    
    Args:
        df: Weather DataFrame
        airport: Airport code
        top_n: Number of top days to return
        
    Returns:
        DataFrame with top windiest days
    """
    # Filter by airport
    airport_df = df[df['origin'] == airport].copy()
    
    # Create date column
    airport_df['date'] = pd.to_datetime(airport_df[['year', 'month', 'day']])
    
    # Calculate daily mean
    daily = airport_df.groupby('date')['wind_speed_ms'].mean().reset_index()
    daily.columns = ['Date', 'Wind_Speed_ms']
    
    # Sort and get top N
    top_days = daily.nlargest(top_n, 'Wind_Speed_ms')
    top_days['Airport'] = airport
    
    return top_days


# =============================================================================
# EXPORT FOR TABLEAU
# =============================================================================

def export_for_tableau(daily: pd.DataFrame, monthly: pd.DataFrame, 
                       top_days: pd.DataFrame, output_dir: str = '.') -> None:
    """
    Export processed data for Tableau.
    
    Args:
        daily: Daily aggregated data
        monthly: Monthly aggregated data
        top_days: Top windiest days data
        output_dir: Output directory
    """
    # Export daily data
    daily.to_csv(f'{output_dir}/daily_wind_speeds.csv', index=False)
    print(f"✓ Exported daily_wind_speeds.csv")
    
    # Export monthly data
    monthly.to_csv(f'{output_dir}/monthly_wind_speeds.csv', index=False)
    print(f"✓ Exported monthly_wind_speeds.csv")
    
    # Export top windiest days
    top_days.to_csv(f'{output_dir}/top_windiest_days.csv', index=False)
    print(f"✓ Exported top_windiest_days.csv")


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def prepare_data_for_tableau(input_file: str, output_dir: str = '.') -> None:
    """
    Main function to prepare all data for Tableau dashboard.
    
    Args:
        input_file: Path to raw weather data
        output_dir: Directory for output files
    """
    print("\n" + "=" * 60)
    print("  DATA PREPARATION FOR TABLEAU DASHBOARD")
    print("=" * 60)
    
    # Step 1: Load and clean data
    print("\n📥 Step 1: Loading and cleaning data...")
    df = load_and_clean_data(input_file)
    
    # Step 2: Calculate daily means
    print("\n📊 Step 2: Calculating daily means...")
    daily = calculate_daily_means(df)
    print(f"   Created {len(daily):,} daily records")
    
    # Step 3: Calculate monthly means
    print("\n📈 Step 3: Calculating monthly means...")
    monthly = calculate_monthly_means(df)
    print(f"   Created {len(monthly)} monthly records")
    
    # Step 4: Find top windiest days
    print("\n🏆 Step 4: Finding top windiest days...")
    top_days = find_top_windiest_days(df, airport='LGA', top_n=20)
    print(f"   Found top {len(top_days)} windiest days at LGA")
    
    # Step 5: Export for Tableau
    print("\n💾 Step 5: Exporting for Tableau...")
    export_for_tableau(daily, monthly, top_days, output_dir)
    
    # Summary
    print("\n" + "=" * 60)
    print("  DATA PREPARATION COMPLETE")
    print("=" * 60)
    print(f"\nFiles created:")
    print(f"  • daily_wind_speeds.csv")
    print(f"  • monthly_wind_speeds.csv")
    print(f"  • top_windiest_days.csv")
    print(f"\nReady for import into Tableau!")
    print("=" * 60)


# =============================================================================
# EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run data preparation
    prepare_data_for_tableau('nycflights13_weather.csv')
