# 🚀 Easy Heroku Deployment Guide

This guide will help you deploy your Dietary Recommendation System to Heroku in just **5 minutes**!

## ✅ Prerequisites

1. **Heroku Account** - Sign up at https://www.heroku.com (Free tier available)
2. **Heroku CLI** - Download from https://devcenter.heroku.com/articles/heroku-cli
3. **Git** - Already installed if you cloned the repo

## 🎯 Step-by-Step Deployment

### Step 1: Install Heroku CLI

**Mac:**
```bash
brew install heroku/brew/heroku
```

**Windows:**
Download and run installer from https://devcenter.heroku.com/articles/heroku-cli

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 2: Login to Heroku

```bash
heroku login
```
This opens a browser to authenticate. Click "Log In" and you're done!

### Step 3: Create Heroku App

```bash
cd dietary-recommendation-system
heroku create your-app-name
```

Replace `your-app-name` with something unique (e.g., `dietary-rec-app-2024`)

Example:
```bash
heroku create dietary-rec-app-2024
```

### Step 4: Deploy Your App

```bash
git push heroku main
```

This takes 2-3 minutes. You'll see build logs in the terminal.

### Step 5: Open Your App

```bash
heroku open
```

Your app is now live! 🎉

---

## 🔍 Verify Deployment

### Check App Status
```bash
heroku ps
```

You should see:
```
Free dyno types are now deprecated...
```

### View Logs
```bash
heroku logs --tail
```

### Check App URL
```bash
heroku info
```

Look for "Web URL" - that's your live app!

---

## ⚙️ Configure Environment Variables (If Needed)

```bash
# Set environment variable
heroku config:set FLASK_ENV=production

# View all variables
heroku config

# Unset a variable
heroku config:unset VARIABLE_NAME
```

---

## 🔧 Troubleshooting

### App Won't Start?
```bash
heroku logs --tail
```
Check the error message and debug.

### Port Error?
The port should be set automatically. If not:
```bash
heroku config:set PORT=5000
```

### Dependencies Not Installing?
Make sure `requirements.txt` is in the root directory:
```bash
ls requirements.txt
```

### Database Errors?
This app doesn't need a database (uses JSON), so you should be fine!

---

## 📊 Monitor Your App

### View Real-Time Logs
```bash
heroku logs --tail
```

### Check Metrics
```bash
heroku logs --num=50  # Last 50 lines
```

### Scale Dynos (Advanced)
```bash
heroku ps:scale web=1
```

---

## 🆙 Update Your App

After making changes:

```bash
# Commit changes
git add .
git commit -m "Your message"

# Deploy
git push heroku main
```

---

## 💰 Pricing

| Tier | Cost | Features |
|------|------|----------|
| **Free** | $0/month | Limited, may sleep |
| **Eco** | $5/month | Always on, shared CPU |
| **Standard** | $7/month | Better performance |

For this project, **Free tier** is perfect!

---

## 🎯 Your App URL

After deployment, your app will be at:
```
https://your-app-name.herokuapp.com
```

Example:
```
https://dietary-rec-app-2024.herokuapp.com
```

---

## ✨ Advanced Options

### Add Custom Domain
```bash
heroku domains:add your-domain.com
```

### Enable Auto-Deploy from GitHub
1. Go to https://dashboard.heroku.com/apps
2. Click your app
3. Go to "Deploy" tab
4. Connect to GitHub
5. Select your repository
6. Click "Enable Automatic Deploys"

### Set Up Monitoring
```bash
heroku addons:create papertrail:choklad
```

---

## 🚨 Common Issues & Solutions

### Issue: "No default language could be detected"
**Solution:** Make sure you have `requirements.txt` in root directory

### Issue: "App crashed"
**Solution:** Check logs with `heroku logs --tail`

### Issue: "Timeout waiting for process to type"
**Solution:** App might be too slow. Try restarting:
```bash
heroku dyno:restart
```

### Issue: "Cannot find module"
**Solution:** Update requirements.txt and redeploy:
```bash
pip freeze > requirements.txt
git push heroku main
```

---

## 🧹 Cleanup

### Delete App
```bash
heroku apps:destroy --app your-app-name
```

### Remove Heroku Remote
```bash
git remote remove heroku
```

---

## 📝 Useful Commands Reference

```bash
heroku login                    # Login
heroku create app-name         # Create app
heroku open                    # Open app in browser
heroku logs --tail             # View live logs
heroku ps                      # Check app status
heroku config                  # View env variables
heroku config:set KEY=VALUE    # Set env variable
git push heroku main           # Deploy
heroku restart                 # Restart app
heroku apps:list              # List all apps
heroku apps:destroy           # Delete app
```

---

## ✅ Deployment Checklist

- [ ] Heroku CLI installed
- [ ] Heroku account created
- [ ] Logged in with `heroku login`
- [ ] Created app with `heroku create`
- [ ] Pushed code with `git push heroku main`
- [ ] App running (check with `heroku open`)
- [ ] Can access at `https://your-app-name.herokuapp.com`

---

## 🎉 Success!

Your app is now live online! 

**Share your app with:**
- Friends: `https://your-app-name.herokuapp.com`
- Social media: Post your live dietary recommendation system
- Portfolio: Add to your GitHub portfolio

---

## 📞 Need Help?

- **Heroku Docs:** https://devcenter.heroku.com/
- **Common Issues:** https://devcenter.heroku.com/articles/troubleshooting-deploys
- **Status Page:** https://status.heroku.com/

---

**Happy Deploying!** 🚀

Your Healthy Dietary Recommendation System is now online! 🥗
