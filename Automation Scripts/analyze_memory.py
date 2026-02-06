#!/usr/bin/env python3
"""
DFIR Lab - Automated Memory Analysis Script
============================================
Purpose: Automate common Volatility3 memory analysis tasks
Author: Ashish Kumar
Date: February 2026

Usage:
    python3 analyze_memory.py -f memory.raw -o output_dir
    python3 analyze_memory.py -f memory.raw -o output_dir --full
"""

import argparse
import subprocess
import os
import sys
import json
from datetime import datetime
from pathlib import Path

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    """Print script banner"""
    banner = f"""
{Colors.OKCYAN}╔══════════════════════════════════════════════════════════════╗
║        DFIR Lab - Automated Memory Analysis Tool            ║
║                  Powered by Volatility3                     ║
╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}
"""
    print(banner)

def run_vol_command(plugin, memory_file, output_dir, output_format='text'):
    """
    Run a Volatility3 plugin and save output
    
    Args:
        plugin: Volatility plugin name
        memory_file: Path to memory dump
        output_dir: Output directory
        output_format: Output format (text, json, csv)
    
    Returns:
        bool: Success status
    """
    output_file = os.path.join(output_dir, f"{plugin}.{output_format}")
    
    print(f"{Colors.OKBLUE}[*] Running {plugin}...{Colors.ENDC}", end=' ')
    
    try:
        if output_format == 'text':
            cmd = ['vol.py', '-f', memory_file, plugin]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            with open(output_file, 'w') as f:
                f.write(result.stdout)
                if result.stderr:
                    f.write("\n\n=== STDERR ===\n")
                    f.write(result.stderr)
        else:
            # For CSV/JSON, use Volatility's render options
            cmd = ['vol.py', '-f', memory_file, '-r', output_format, plugin]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            with open(output_file, 'w') as f:
                f.write(result.stdout)
        
        if result.returncode == 0:
            print(f"{Colors.OKGREEN}✓ Complete{Colors.ENDC}")
            return True
        else:
            print(f"{Colors.FAIL}✗ Failed{Colors.ENDC}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"{Colors.WARNING}⏱ Timeout{Colors.ENDC}")
        return False
    except Exception as e:
        print(f"{Colors.FAIL}✗ Error: {str(e)}{Colors.ENDC}")
        return False

def get_memory_info(memory_file):
    """Get basic information about memory dump"""
    try:
        size_mb = os.path.getsize(memory_file) / (1024 * 1024)
        return {
            'file': os.path.basename(memory_file),
            'path': os.path.abspath(memory_file),
            'size_mb': round(size_mb, 2),
            'timestamp': datetime.fromtimestamp(os.path.getmtime(memory_file)).strftime('%Y-%m-%d %H:%M:%S')
        }
    except Exception as e:
        return {'error': str(e)}

def analyze_memory(memory_file, output_dir, full_analysis=False):
    """
    Perform memory analysis
    
    Args:
        memory_file: Path to memory dump
        output_dir: Output directory
        full_analysis: Perform full analysis (slower)
    """
    
    # Basic plugins (fast)
    basic_plugins = [
        'windows.info',           # System info
        'windows.pslist',         # Process list
        'windows.psscan',         # Scan for processes
        'windows.pstree',         # Process tree
        'windows.cmdline',        # Command lines
        'windows.netscan',        # Network connections
        'windows.netstat',        # Network statistics
        'windows.dlllist',        # DLL list
        'windows.handles',        # Open handles
        'windows.filescan',       # File objects
    ]
    
    # Extended plugins (slower)
    extended_plugins = [
        'windows.malfind',        # Malware detection
        'windows.ldrmodules',     # Module information
        'windows.ssdt',           # System Service Descriptor Table
        'windows.driverscan',     # Driver scan
        'windows.modscan',        # Module scan
        'windows.mutantscan',     # Mutant scan
        'windows.registry.hivelist',  # Registry hives
        'windows.registry.printkey',  # Registry keys
        'windows.svcscan',        # Service scan
    ]
    
    plugins = basic_plugins + (extended_plugins if full_analysis else [])
    
    results = {
        'success': [],
        'failed': [],
        'total': len(plugins)
    }
    
    print(f"\n{Colors.HEADER}Starting analysis of {os.path.basename(memory_file)}...{Colors.ENDC}")
    print(f"Output directory: {output_dir}\n")
    
    for plugin in plugins:
        success = run_vol_command(plugin, memory_file, output_dir)
        if success:
            results['success'].append(plugin)
        else:
            results['failed'].append(plugin)
    
    return results

def generate_report(memory_file, output_dir, results, analysis_info):
    """Generate summary report"""
    report_file = os.path.join(output_dir, 'analysis_report.txt')
    
    with open(report_file, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("DFIR Lab - Memory Analysis Report\n")
        f.write("=" * 70 + "\n\n")
        
        f.write("Analysis Information:\n")
        f.write("-" * 70 + "\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Memory Dump: {analysis_info['file']}\n")
        f.write(f"File Size: {analysis_info['size_mb']} MB\n")
        f.write(f"Dump Created: {analysis_info['timestamp']}\n\n")
        
        f.write("Analysis Results:\n")
        f.write("-" * 70 + "\n")
        f.write(f"Total Plugins Run: {results['total']}\n")
        f.write(f"Successful: {len(results['success'])}\n")
        f.write(f"Failed: {len(results['failed'])}\n\n")
        
        if results['success']:
            f.write("Successfully Completed Plugins:\n")
            for plugin in results['success']:
                f.write(f"  ✓ {plugin}\n")
            f.write("\n")
        
        if results['failed']:
            f.write("Failed Plugins:\n")
            for plugin in results['failed']:
                f.write(f"  ✗ {plugin}\n")
            f.write("\n")
        
        f.write("Output Files:\n")
        f.write("-" * 70 + "\n")
        for file in sorted(os.listdir(output_dir)):
            if file != 'analysis_report.txt':
                file_path = os.path.join(output_dir, file)
                size = os.path.getsize(file_path)
                f.write(f"  {file} ({size} bytes)\n")
        
        f.write("\n" + "=" * 70 + "\n")
        f.write("Analysis complete!\n")
        f.write("=" * 70 + "\n")
    
    print(f"\n{Colors.OKGREEN}✓ Report generated: {report_file}{Colors.ENDC}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Automated Volatility3 Memory Analysis Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Basic analysis:
    python3 analyze_memory.py -f memory.raw -o output_dir
  
  Full analysis (includes malware detection):
    python3 analyze_memory.py -f memory.raw -o output_dir --full
  
  Specify output format:
    python3 analyze_memory.py -f memory.raw -o output_dir --format csv
        """
    )
    
    parser.add_argument(
        '-f', '--file',
        required=True,
        help='Path to memory dump file'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output directory for results'
    )
    
    parser.add_argument(
        '--full',
        action='store_true',
        help='Perform full analysis (slower, includes malware detection)'
    )
    
    parser.add_argument(
        '--format',
        choices=['text', 'csv', 'json'],
        default='text',
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--no-report',
        action='store_true',
        help='Skip report generation'
    )
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Verify memory file exists
    if not os.path.exists(args.file):
        print(f"{Colors.FAIL}Error: Memory file not found: {args.file}{Colors.ENDC}")
        sys.exit(1)
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Get memory file info
    mem_info = get_memory_info(args.file)
    
    # Print analysis info
    print(f"{Colors.HEADER}Memory Dump Information:{Colors.ENDC}")
    print(f"  File: {mem_info['file']}")
    print(f"  Size: {mem_info['size_mb']} MB")
    print(f"  Created: {mem_info['timestamp']}")
    
    # Perform analysis
    results = analyze_memory(args.file, args.output, args.full)
    
    # Generate report
    if not args.no_report:
        generate_report(args.file, args.output, results, mem_info)
    
    # Print summary
    print(f"\n{Colors.HEADER}Analysis Summary:{Colors.ENDC}")
    print(f"  {Colors.OKGREEN}Successful: {len(results['success'])}{Colors.ENDC}")
    print(f"  {Colors.FAIL}Failed: {len(results['failed'])}{Colors.ENDC}")
    print(f"  Total: {results['total']}")
    
    if results['failed']:
        print(f"\n{Colors.WARNING}⚠ Some plugins failed. Check output files for details.{Colors.ENDC}")
    
    print(f"\n{Colors.OKGREEN}✓ Analysis complete! Results saved to: {args.output}{Colors.ENDC}\n")

if __name__ == '__main__':
    main()
