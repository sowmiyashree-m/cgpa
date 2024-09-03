def cgpaCalculator():

	TotalScoreOfferable = 0
	
	obtainedGrade = 0

	
	numberOfCourses = int(input(" Enter the number of Courses you studied: "))
	
	for x in range(numberOfCourses):
		
		Course1 = input("Enter The Course code :")
		
		unit = int(input ("No.of units you studied in that course: "))
	
		score = int(input("Please Enter your Score out of 100:"))

		
		TotalScoreOfferable += unit* 5


		if (score >= 70):
			grade = 5
		elif(score < 70 and  score >= 60):
			grade = 4 
		elif(score < 60 and  score >= 50 ):
			grade = 3
		elif(score < 50 and  score >=45):
			grade = 2
		elif (score < 45 and  score>=40):
			grade = 1
		else :
			grade = 0 


		obtainedGrade += unit*grade

	Cgpa =float((obtainedGrade / TotalScoreOfferable) * 5)
	print(" YOUR CGPA IS : " + str(Cgpa))


cgpaCalculator()
