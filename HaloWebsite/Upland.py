import requests
import json



def UserProfile(userName):
	#myToken='eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJ1c2VySWQiOiJmMDRlMjhiMC1iZWJhLTExZWEtOTFjMS1lNWI0YmNkOGQwZjEiLCJ2YWxpZGF0aW9uVG9rZW4iOiJtVVJlbkRzUXZsZE9sUm4zY3g4T0lHNndRZWtTN1U0ckdiVHdSZWhpaXdJIiwiaWF0IjoxNTkzOTUyMDk2LCJleHAiOjE2MjU1MDk2OTYsImF1ZCI6Imh0dHBzOi8veW91cmRvbWFpbi5jb20iLCJpc3MiOiJmZWF0aGVycyIsInN1YiI6ImFub255bW91cyIsImp0aSI6IjNmNDk5MmEzLTY2ZDMtNGY4NS1iYjlkLTNkNDkxYjJmYzUzNiJ9.DNeuiQNczHltdBz2w6PAYUn2v9ZfxzjHNSb1qOeK_Fo'
	myToken='eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJ1c2VySWQiOiJhOWI0NDFmMC1lNzBmLTExZWEtYmE3Mi1mZjFjNTE1NWJhNWQiLCJ2YWxpZGF0aW9uVG9rZW4iOm51bGwsImlhdCI6MTU5ODM4NjU0MywiZXhwIjoxNjI5OTQ0MTQzLCJpc3MiOiJmZWF0aGVycyIsInN1YiI6ImE5YjQ0MWYwLWU3MGYtMTFlYS1iYTcyLWZmMWM1MTU1YmE1ZCIsImp0aSI6ImU3NjJhZTIwLWI5MmItNGVhOS05MTM4LWY5ZjdkZTZkYzZjZCJ9.tW17d8co8dqibFbTKEk-eOhhSnJZXUoQqhCaqU-PW8Q'
	headers 		= {'authorization' : myToken }
	profile 	= requests.get('https://api.upland.me/profile/{0}'.format(userName), headers=headers)
	userProfile	= profile.json()
	#image		= userProfile['avatar']['image']
	#userProfile.add(image)
	#image		= userProfile['avatar']['image']

	
	return userProfile
