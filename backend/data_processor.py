"""
Data Processor Module
=====================
This module handles all data loading, processing, and context retrieval
for the Fund Data Chatbot application.

It loads holdings and trades CSV files and provides methods to:
- Get data summaries and statistics
- Extract relevant context for questions
- Calculate fund performance metrics
- Handle data queries and filtering

Author: Fund Data Chatbot Team
Date: 2026-01-09
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Any
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class DataProcessor:
    """
    Handles all data processing operations for the Fund Data Chatbot.
    
    Attributes:
        holdings_df (pd.DataFrame): DataFrame containing holdings data
        trades_df (pd.DataFrame): DataFrame containing trades data
        data_loaded (bool): Flag indicating if data has been successfully loaded
    """
    
    def __init__(self):
        """Initialize the DataProcessor and load CSV files."""
        self.holdings_df = None
        self.trades_df = None
        self.data_loaded = False
        self._load_data()
    
    def _load_data(self):
        """
        Load holdings and trades CSV files into pandas DataFrames.
        
        Raises:
            FileNotFoundError: If CSV files are not found
            Exception: For other data loading errors
        """
        try:
            # Determine the data directory (parent of backend)
            backend_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.dirname(backend_dir)
            
            holdings_path = os.path.join(data_dir, 'holdings.csv')
            trades_path = os.path.join(data_dir, 'trades.csv')
            
            # Check if files exist
            if not os.path.exists(holdings_path):
                raise FileNotFoundError(f"Holdings file not found: {holdings_path}")
            if not os.path.exists(trades_path):
                raise FileNotFoundError(f"Trades file not found: {trades_path}")
            
            # Load CSV files
            logger.info("Loading holdings data...")
            self.holdings_df = pd.read_csv(holdings_path)
            
            logger.info("Loading trades data...")
            self.trades_df = pd.read_csv(trades_path)
            
            # Convert numeric columns
            self._convert_numeric_columns()
            
            self.data_loaded = True
            logger.info(f"Data loaded successfully - Holdings: {len(self.holdings_df)} rows, Trades: {len(self.trades_df)} rows")
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            self.data_loaded = False
            raise
    
    def _convert_numeric_columns(self):
        """Convert numeric columns to appropriate data types."""
        # Holdings numeric columns
        holdings_numeric = ['StartQty', 'Qty', 'StartPrice', 'Price', 'StartFXRate', 'FXRate',
                           'MV_Local', 'MV_Base', 'PL_DTD', 'PL_QTD', 'PL_MTD', 'PL_YTD']
        for col in holdings_numeric:
            if col in self.holdings_df.columns:
                self.holdings_df[col] = pd.to_numeric(self.holdings_df[col], errors='coerce')
        
        # Trades numeric columns
        trades_numeric = ['Quantity', 'Price', 'TradeFXRate', 'Principal', 'Interest',
                         'TotalCash', 'AllocationQTY', 'AllocationPrincipal',
                         'AllocationInterest', 'AllocationFees', 'AllocationCash']
        for col in trades_numeric:
            if col in self.trades_df.columns:
                self.trades_df[col] = pd.to_numeric(self.trades_df[col], errors='coerce')
    
    def get_data_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive summary of the loaded data.
        
        Returns:
            Dictionary containing summary statistics and metadata
        """
        if not self.data_loaded:
            return {'error': 'Data not loaded'}
        
        # Get unique funds from both datasets
        holdings_funds = self.holdings_df['PortfolioName'].unique().tolist() if 'PortfolioName' in self.holdings_df.columns else []
        trades_funds = self.trades_df['PortfolioName'].unique().tolist() if 'PortfolioName' in self.trades_df.columns else []
        unique_funds = sorted(list(set(holdings_funds + trades_funds)))
        
        summary = {
            'holdings': {
                'total_records': len(self.holdings_df),
                'unique_funds': len(holdings_funds),
                'unique_securities': self.holdings_df['SecurityTypeName'].nunique() if 'SecurityTypeName' in self.holdings_df.columns else 0,
                'date_range': {
                    'start': self.holdings_df['AsOfDate'].min() if 'AsOfDate' in self.holdings_df.columns else None,
                    'end': self.holdings_df['AsOfDate'].max() if 'AsOfDate' in self.holdings_df.columns else None
                },
                'total_market_value': float(self.holdings_df['MV_Base'].sum()) if 'MV_Base' in self.holdings_df.columns else 0,
                'columns': list(self.holdings_df.columns)
            },
            'trades': {
                'total_records': len(self.trades_df),
                'unique_funds': len(trades_funds),
                'trade_types': self.trades_df['TradeTypeName'].unique().tolist() if 'TradeTypeName' in self.trades_df.columns else [],
                'total_principal': float(self.trades_df['Principal'].sum()) if 'Principal' in self.trades_df.columns else 0,
                'columns': list(self.trades_df.columns)
            },
            'funds': unique_funds,
            'data_loaded': self.data_loaded,
            'last_updated': datetime.now().isoformat()
        }
        
        return summary
    
    def get_unique_funds(self) -> List[str]:
        """
        Get list of all unique fund names.
        
        Returns:
            Sorted list of unique fund names
        """
        if not self.data_loaded:
            return []
        
        holdings_funds = self.holdings_df['PortfolioName'].unique().tolist() if 'PortfolioName' in self.holdings_df.columns else []
        trades_funds = self.trades_df['PortfolioName'].unique().tolist() if 'PortfolioName' in self.trades_df.columns else []
        unique_funds = sorted(list(set(holdings_funds + trades_funds)))
        
        return unique_funds
    
    def get_fund_performance(self, fund_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Calculate fund performance metrics.
        
        Args:
            fund_name: Specific fund to analyze (None for all funds)
        
        Returns:
            Dictionary with performance metrics
        """
        if not self.data_loaded:
            return {'error': 'Data not loaded'}
        
        try:
            if fund_name:
                holdings = self.holdings_df[self.holdings_df['PortfolioName'] == fund_name]
            else:
                holdings = self.holdings_df
            
            if len(holdings) == 0:
                return {'error': f'No data found for fund: {fund_name}'}
            
            performance = {
                'fund_name': fund_name or 'All Funds',
                'total_holdings': len(holdings),
                'total_market_value': float(holdings['MV_Base'].sum()) if 'MV_Base' in holdings.columns else 0,
                'profit_loss_ytd': float(holdings['PL_YTD'].sum()) if 'PL_YTD' in holdings.columns else 0,
                'profit_loss_mtd': float(holdings['PL_MTD'].sum()) if 'PL_MTD' in holdings.columns else 0,
                'profit_loss_qtd': float(holdings['PL_QTD'].sum()) if 'PL_QTD' in holdings.columns else 0,
                'profit_loss_dtd': float(holdings['PL_DTD'].sum()) if 'PL_DTD' in holdings.columns else 0
            }
            
            return performance
            
        except Exception as e:
            logger.error(f"Error calculating fund performance: {str(e)}")
            return {'error': str(e)}
    
    def get_relevant_context(self, question: str) -> str:
        """
        Extract relevant data context based on the question.
        
        This method analyzes the question and returns relevant data snippets
        that can be used as context for the LLM.
        
        Args:
            question: The user's question
        
        Returns:
            Formatted string containing relevant data context
        """
        if not self.data_loaded:
            return "No relevant data found."
        
        question_lower = question.lower()
        context_parts = []
        
        try:
            # Add general data summary
            context_parts.append("=== FUND DATA SUMMARY ===")
            summary = self.get_data_summary()
            context_parts.append(f"Total Holdings Records: {summary['holdings']['total_records']}")
            context_parts.append(f"Total Trades Records: {summary['trades']['total_records']}")
            context_parts.append(f"Available Funds: {', '.join(summary['funds'][:10])}{'...' if len(summary['funds']) > 10 else ''}")
            context_parts.append("")
            
            # Check for specific fund mentions
            mentioned_funds = [fund for fund in self.get_unique_funds() if fund.lower() in question_lower]
            
            # Handle performance-related questions
            if any(keyword in question_lower for keyword in ['perform', 'profit', 'loss', 'p&l', 'p/l', 'better', 'best', 'worst', 'ytd', 'year']):
                context_parts.append("=== FUND PERFORMANCE (Profit/Loss YTD) ===")
                
                if mentioned_funds:
                    # Show specific funds
                    for fund in mentioned_funds:
                        perf = self.get_fund_performance(fund)
                        if 'error' not in perf:
                            context_parts.append(f"\nFund: {fund}")
                            context_parts.append(f"  Total Holdings: {perf['total_holdings']}")
                            context_parts.append(f"  Market Value: ${perf['total_market_value']:,.2f}")
                            context_parts.append(f"  P&L YTD: ${perf['profit_loss_ytd']:,.2f}")
                            context_parts.append(f"  P&L QTD: ${perf['profit_loss_qtd']:,.2f}")
                            context_parts.append(f"  P&L MTD: ${perf['profit_loss_mtd']:,.2f}")
                else:
                    # Show all funds performance summary
                    funds_performance = []
                    for fund in self.get_unique_funds():
                        perf = self.get_fund_performance(fund)
                        if 'error' not in perf and perf['profit_loss_ytd'] != 0:
                            funds_performance.append({
                                'fund': fund,
                                'pl_ytd': perf['profit_loss_ytd'],
                                'holdings': perf['total_holdings']
                            })
                    
                    # Sort by P&L YTD
                    funds_performance.sort(key=lambda x: x['pl_ytd'], reverse=True)
                    
                    for fp in funds_performance[:15]:  # Top 15 funds
                        context_parts.append(f"\nFund: {fp['fund']}")
                        context_parts.append(f"  Holdings: {fp['holdings']}")
                        context_parts.append(f"  P&L YTD: ${fp['pl_ytd']:,.2f}")
                
                context_parts.append("")
            
            # Handle count/total questions
            if any(keyword in question_lower for keyword in ['how many', 'total', 'count', 'number of']):
                if 'holding' in question_lower:
                    context_parts.append("=== HOLDINGS COUNT BY FUND ===")
                    holdings_by_fund = self.holdings_df.groupby('PortfolioName').size().to_dict()
                    
                    if mentioned_funds:
                        for fund in mentioned_funds:
                            count = holdings_by_fund.get(fund, 0)
                            context_parts.append(f"{fund}: {count} holdings")
                    else:
                        for fund, count in sorted(holdings_by_fund.items(), key=lambda x: x[1], reverse=True)[:20]:
                            context_parts.append(f"{fund}: {count} holdings")
                    context_parts.append("")
                
                if 'trade' in question_lower:
                    context_parts.append("=== TRADES COUNT BY FUND ===")
                    trades_by_fund = self.trades_df.groupby('PortfolioName').size().to_dict()
                    
                    if mentioned_funds:
                        for fund in mentioned_funds:
                            count = trades_by_fund.get(fund, 0)
                            context_parts.append(f"{fund}: {count} trades")
                    else:
                        for fund, count in sorted(trades_by_fund.items(), key=lambda x: x[1], reverse=True)[:20]:
                            context_parts.append(f"{fund}: {count} trades")
                    context_parts.append("")
            
            # If specific funds mentioned, add their detailed data
            if mentioned_funds:
                for fund in mentioned_funds[:3]:  # Limit to 3 funds
                    context_parts.append(f"\n=== DETAILED DATA FOR {fund.upper()} ===")
                    
                    # Holdings sample
                    fund_holdings = self.holdings_df[self.holdings_df['PortfolioName'] == fund]
                    if len(fund_holdings) > 0:
                        context_parts.append(f"\nHoldings Sample (showing {min(5, len(fund_holdings))} of {len(fund_holdings)} records):")
                        context_parts.append(fund_holdings.head(5).to_string())
                    
                    # Trades sample
                    fund_trades = self.trades_df[self.trades_df['PortfolioName'] == fund]
                    if len(fund_trades) > 0:
                        context_parts.append(f"\nTrades Sample (showing {min(5, len(fund_trades))} of {len(fund_trades)} records):")
                        context_parts.append(fund_trades.head(5).to_string())
            
            # If no specific context was added, provide general samples
            if len(context_parts) <= 5:
                context_parts.append("\n=== SAMPLE DATA ===")
                context_parts.append("\nHoldings Sample:")
                context_parts.append(self.holdings_df.head(10).to_string())
                context_parts.append("\nTrades Sample:")
                context_parts.append(self.trades_df.head(10).to_string())
            
            # Add important note
            context_parts.append("\n=== IMPORTANT ===")
            context_parts.append("Only use the data provided above to answer questions.")
            context_parts.append("If the answer cannot be found in this data, respond with: 'Sorry, I cannot find the answer in the provided fund data.'")
            
            return "\n".join(context_parts)
            
        except Exception as e:
            logger.error(f"Error getting relevant context: {str(e)}")
            return f"Error retrieving context: {str(e)}"
