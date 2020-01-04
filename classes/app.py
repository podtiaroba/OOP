from models.recrut_progr import Recruiter, Programer
from models.candidat_vacancy import Candidat, Vacancy

def main():

	recr = Recruiter('Petya', 'vksk', 1234, 50, '11-00')
	progr1 = Programer('Dima', 'pppp', 4321, 100, '12-00')
	progr2 = Programer('Ira', 'prprpr', 7892, 100, '13-00')
	cand1 = Candidat('Dan', 'wwww', 'Python', 4, 5)
	cand2 = Candidat('Kirill', 'wwww', 'Recruting', 5, 4)
	cand3 = Candidat('Alex', 'wwww', 'C++', 5, 3)
	vac1 = Vacancy('Python', 5, 5)
	vac2 = Vacancy('Recruting', 5, 4)
	