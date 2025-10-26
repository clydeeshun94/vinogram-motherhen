#!/usr/bin/env python3
"""
Deployment script for MotherHen application.
This script builds the frontend and starts the backend server.
"""

import os
import subprocess
import sys
import shutil

def build_frontend():
    """Build the React frontend"""
    print("Building React frontend...")
    try:
        # Check if node is installed
        subprocess.run(['node', '--version'], check=True, capture_output=True)
        subprocess.run(['npm', '--version'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Error: Node.js and npm are required to build the frontend.")
        print("Please install Node.js from https://nodejs.org/")
        return False
    except FileNotFoundError:
        print("Error: Node.js and npm are not found in PATH.")
        print("Please install Node.js from https://nodejs.org/")
        return False

    # Change to frontend directory
    frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')
    if not os.path.exists(frontend_dir):
        print("Error: Frontend directory not found.")
        return False

    try:
        # Install dependencies
        print("Installing frontend dependencies...")
        subprocess.run(['npm', 'install'], cwd=frontend_dir, check=True)
        
        # Build frontend
        print("Building frontend...")
        subprocess.run(['npm', 'run', 'build'], cwd=frontend_dir, check=True)
        
        print("Frontend built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error building frontend: {e}")
        return False

def start_backend():
    """Start the Python backend"""
    print("Starting Python backend...")
    backend_script = os.path.join(os.path.dirname(__file__), 'backend', 'main.py')
    
    if not os.path.exists(backend_script):
        print("Error: Backend script not found.")
        return False
    
    try:
        subprocess.run(['python', backend_script], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error starting backend: {e}")
        return False
    except KeyboardInterrupt:
        print("\nShutting down...")
        return True

def main():
    """Main deployment function"""
    print("MotherHen Deployment Script")
    print("=" * 30)
    
    # Build frontend
    if not build_frontend():
        print("Failed to build frontend. Exiting.")
        sys.exit(1)
    
    # Start backend
    if not start_backend():
        print("Failed to start backend.")
        sys.exit(1)

if __name__ == "__main__":
    main()