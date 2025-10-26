#!/usr/bin/env python3
"""
Local deployment test script - simulates Vercel environment
"""

import os
import sys

def test_vercel_setup():
    print("🧪 Testing Vercel Deployment Setup")
    print("=" * 50)
    
    # Set environment variables to simulate Vercel
    os.environ["VERCEL_ENV"] = "production"
    os.environ["FLASK_ENV"] = "production"
    
    try:
        # Test import
        from api.index import app
        print("✅ API entry point imports successfully")
        
        # Test app creation
        with app.app_context():
            print("✅ Flask app context works")
            
            # Test routes
            with app.test_client() as client:
                response = client.get('/')
                print(f"✅ Home route responds: {response.status_code}")
                
                response = client.get('/api/skills/search?q=python')
                print(f"✅ API route responds: {response.status_code}")
        
        # Test configuration
        print(f"✅ Database URI configured: {app.config['SQLALCHEMY_DATABASE_URI'][:20]}...")
        print(f"✅ Secret key configured: {'Yes' if app.config['SECRET_KEY'] else 'No'}")
        
        print("\n🎉 Vercel setup test passed!")
        print("Ready to deploy with: vercel --prod")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Troubleshooting:")
        print("1. Check all imports are working")
        print("2. Verify api/index.py exists")
        print("3. Ensure requirements.txt is complete")
        return False
    
    return True

if __name__ == "__main__":
    success = test_vercel_setup()
    if not success:
        sys.exit(1)
