import sqlite3

# Database setup
connection=sqlite3.connect("student.db")

# Create cursor
cursor=connection.cursor()

# Create the table
create_table_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME    VARCHAR(25),
    COURSE   VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

cursor.execute(create_table_query)

# Insert Records
sql_query = """INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?, ?, ?, ?)"""
values = [('Student1', 'Data Science', 'C', 61)
,
('Student2', 'DEVOPS', 'E', 50)
,
('Student3', 'Data Science', 'C', 40)
,
('Student4', 'DEVOPS', 'C', 36)
,
('Student5', 'DEVOPS', 'E', 96)
,
('Student6', 'Cloud Computing', 'A', 37)
,
('Student7', 'DEVOPS', 'C', 51)
,
('Student8', 'DEVOPS', 'A', 85)
,
('Student9', 'DEVOPS', 'D', 32)
,
('Student10', 'AI', 'B', 54)
,
('Student11', 'DEVOPS', 'D', 66)
,
('Student12', 'Cyber Security', 'A', 52)
,
('Student13', 'Data Science', 'D', 72)
,
('Student14', 'AI', 'B', 45)
,
('Student15', 'Cyber Security', 'E', 65)
,
('Student16', 'Data Science', 'D', 91)
,
('Student17', 'Data Science', 'B', 79)
,
('Student18', 'AI', 'D', 77)
,
('Student19', 'DEVOPS', 'A', 49)
,
('Student20', 'AI', 'C', 78)
,
('Student21', 'DEVOPS', 'B', 73)
,
('Student22', 'AI', 'A', 69)
,
('Student23', 'AI', 'A', 58)
,
('Student24', 'AI', 'A', 34)
,
('Student25', 'Cyber Security', 'A', 46)
,
('Student26', 'Cyber Security', 'D', 50)
,
('Student27', 'AI', 'C', 76)
,
('Student28', 'DEVOPS', 'B', 97)
,
('Student29', 'AI', 'A', 39)
,
('Student30', 'Cyber Security', 'E', 83)
,
('Student31', 'Cloud Computing', 'A', 66)
,
('Student32', 'DEVOPS', 'B', 30)
,
('Student33', 'DEVOPS', 'C', 48)
,
('Student34', 'Cyber Security', 'D', 46)
,
('Student35', 'Data Science', 'B', 72)
,
('Student36', 'Cloud Computing', 'E', 46)
,
('Student37', 'AI', 'C', 49)
,
('Student38', 'Cloud Computing', 'B', 31)
,
('Student39', 'Data Science', 'C', 60)
,
('Student40', 'Data Science', 'A', 48)
,
('Student41', 'AI', 'B', 40)
,
('Student42', 'Cyber Security', 'A', 95)
,
('Student43', 'AI', 'E', 62)
,
('Student44', 'Data Science', 'E', 55)
,
('Student45', 'AI', 'C', 49)
,
('Student46', 'Data Science', 'A', 52)
,
('Student47', 'Data Science', 'B', 51)
,
('Student48', 'DEVOPS', 'A', 91)
,
('Student49', 'Data Science', 'D', 94)
,
('Student50', 'Cyber Security', 'C', 82)
,
('Student51', 'Cyber Security', 'A', 72)
,
('Student52', 'AI', 'C', 83)
,
('Student53', 'Data Science', 'B', 39)
,
('Student54', 'Data Science', 'A', 58)
,
('Student55', 'Data Science', 'D', 80)
,
('Student56', 'Cyber Security', 'A', 95)
,
('Student57', 'Cyber Security', 'D', 97)
,
('Student58', 'Data Science', 'E', 45)
,
('Student59', 'AI', 'A', 52)
,
('Student60', 'DEVOPS', 'D', 56)
,
('Student61', 'Data Science', 'C', 44)
,
('Student62', 'Cyber Security', 'C', 62)
,
('Student63', 'Cyber Security', 'A', 56)
,
('Student64', 'AI', 'A', 34)
,
('Student65', 'DEVOPS', 'C', 37)
,
('Student66', 'Cyber Security', 'C', 32)
,
('Student67', 'DEVOPS', 'D', 76)
,
('Student68', 'Cloud Computing', 'A', 73)
,
('Student69', 'AI', 'A', 43)
,
('Student70', 'AI', 'C', 69)
,
('Student71', 'AI', 'E', 87)
,
('Student72', 'AI', 'A', 52)
,
('Student73', 'Cloud Computing', 'C', 32)
,
('Student74', 'DEVOPS', 'D', 71)
,
('Student75', 'AI', 'A', 68)
,
('Student76', 'Cloud Computing', 'B', 34)
,
('Student77', 'AI', 'B', 34)
,
('Student78', 'DEVOPS', 'B', 47)
,
('Student79', 'AI', 'B', 35)
,
('Student80', 'DEVOPS', 'B', 97)
,
('Student81', 'Cyber Security', 'E', 34)
,
('Student82', 'Data Science', 'C', 79)
,
('Student83', 'AI', 'B', 50)
,
('Student84', 'DEVOPS', 'B', 47)
,
('Student85', 'Cyber Security', 'A', 30)
,
('Student86', 'Cyber Security', 'E', 77)
,
('Student87', 'Cloud Computing', 'C', 91)
,
('Student88', 'AI', 'C', 69)
,
('Student89', 'Data Science', 'B', 49)
,
('Student90', 'AI', 'C', 35)
,
('Student91', 'AI', 'B', 65)
,
('Student92', 'Data Science', 'A', 95)
,
('Student93', 'Cloud Computing', 'B', 83)
,
('Student94', 'Cloud Computing', 'B', 36)
,
('Student95', 'Cyber Security', 'B', 32)
,
('Student96', 'Data Science', 'C', 41)
,
('Student97', 'Cyber Security', 'D', 35)
,
('Student98', 'Data Science', 'C', 47)
,
('Student99', 'DEVOPS', 'D', 78)
,
('Student100', 'DEVOPS', 'D', 67)
,
('Student101', 'AI', 'D', 30)
,
('Student102', 'Cyber Security', 'B', 77)
,
('Student103', 'DEVOPS', 'E', 74)
,
('Student104', 'Data Science', 'D', 96)
,
('Student105', 'Cloud Computing', 'A', 63)
,
('Student106', 'DEVOPS', 'D', 94)
,
('Student107', 'Cyber Security', 'B', 93)
,
('Student108', 'Cyber Security', 'E', 31)
,
('Student109', 'AI', 'B', 45)
,
('Student110', 'Cyber Security', 'E', 73)
,
('Student111', 'AI', 'C', 95)
,
('Student112', 'Cloud Computing', 'A', 57)
,
('Student113', 'Cloud Computing', 'C', 35)
,
('Student114', 'Data Science', 'E', 74)
,
('Student115', 'Data Science', 'E', 65)
,
('Student116', 'Cyber Security', 'E', 78)
,
('Student117', 'Cyber Security', 'B', 81)
,
('Student118', 'AI', 'C', 59)
,
('Student119', 'DEVOPS', 'E', 69)
,
('Student120', 'Data Science', 'E', 30)
,
('Student121', 'Cloud Computing', 'B', 71)
,
('Student122', 'Cloud Computing', 'B', 86)
,
('Student123', 'Cyber Security', 'D', 86)
,
('Student124', 'Data Science', 'A', 41)
,
('Student125', 'AI', 'E', 95)
,
('Student126', 'Data Science', 'B', 62)
,
('Student127', 'Cloud Computing', 'A', 51)
,
('Student128', 'AI', 'C', 34)
,
('Student129', 'Cloud Computing', 'E', 54)
,
('Student130', 'Cyber Security', 'A', 97)
,
('Student131', 'AI', 'B', 73)
,
('Student132', 'Cyber Security', 'E', 40)
,
('Student133', 'DEVOPS', 'D', 68)
,
('Student134', 'Data Science', 'C', 89)
,
('Student135', 'Data Science', 'B', 52)
,
('Student136', 'Cyber Security', 'D', 42)
,
('Student137', 'DEVOPS', 'A', 74)
,
('Student138', 'Cyber Security', 'D', 45)
,
('Student139', 'Cyber Security', 'E', 61)
,
('Student140', 'Cloud Computing', 'A', 35)
,
('Student141', 'AI', 'D', 49)
,
('Student142', 'Cyber Security', 'B', 45)
,
('Student143', 'Cloud Computing', 'E', 33)
,
('Student144', 'Cyber Security', 'D', 59)
,
('Student145', 'DEVOPS', 'D', 83)
,
('Student146', 'Cyber Security', 'D', 48)
,
('Student147', 'Cloud Computing', 'A', 90)
,
('Student148', 'Cloud Computing', 'B', 50)
,
('Student149', 'Data Science', 'B', 63)
,
('Student150', 'DEVOPS', 'C', 67)
,
('Student151', 'Cloud Computing', 'D', 56)
,
('Student152', 'Cloud Computing', 'E', 38)
,
('Student153', 'Cloud Computing', 'C', 92)
,
('Student154', 'Cloud Computing', 'C', 66)
,
('Student155', 'AI', 'B', 76)
,
('Student156', 'AI', 'E', 44)
,
('Student157', 'AI', 'B', 67)
,
('Student158', 'Data Science', 'A', 97)
,
('Student159', 'Data Science', 'E', 47)
,
('Student160', 'DEVOPS', 'A', 83)
,
('Student161', 'DEVOPS', 'C', 41)
,
('Student162', 'Cyber Security', 'A', 40)
,
('Student163', 'Data Science', 'E', 66)
,
('Student164', 'Cloud Computing', 'C', 56)
,
('Student165', 'Data Science', 'E', 81)
,
('Student166', 'Cloud Computing', 'D', 89)
,
('Student167', 'AI', 'C', 83)
,
('Student168', 'Cyber Security', 'C', 33)
,
('Student169', 'Cloud Computing', 'A', 55)
,
('Student170', 'AI', 'B', 68)
,
('Student171', 'Cyber Security', 'D', 53)
,
('Student172', 'DEVOPS', 'E', 71)
,
('Student173', 'Cyber Security', 'B', 38)
,
('Student174', 'Cloud Computing', 'A', 58)
,
('Student175', 'AI', 'D', 85)
,
('Student176', 'DEVOPS', 'C', 74)
,
('Student177', 'Data Science', 'E', 54)
,
('Student178', 'Data Science', 'D', 66)
,
('Student179', 'Cloud Computing', 'C', 83)
,
('Student180', 'DEVOPS', 'D', 78)
,
('Student181', 'Cloud Computing', 'A', 36)
,
('Student182', 'Cloud Computing', 'A', 37)
,
('Student183', 'Cyber Security', 'D', 85)
,
('Student184', 'Cyber Security', 'D', 60)
,
('Student185', 'AI', 'E', 84)
,
('Student186', 'Data Science', 'D', 50)
,
('Student187', 'Data Science', 'D', 100)
,
('Student188', 'Data Science', 'C', 46)
,
('Student189', 'AI', 'B', 51)
,
('Student190', 'DEVOPS', 'B', 74)
,
('Student191', 'Data Science', 'C', 61)
,
('Student192', 'AI', 'B', 73)
,
('Student193', 'Cloud Computing', 'A', 49)
,
('Student194', 'Cyber Security', 'A', 41)
,
('Student195', 'Data Science', 'D', 67)
,
('Student196', 'AI', 'A', 81)
,
('Student197', 'DEVOPS', 'B', 71)
,
('Student198', 'DEVOPS', 'B', 43)
,
('Student199', 'Cloud Computing', 'E', 84)
,
('Student200', 'DEVOPS', 'A', 69)
,
('Student201', 'AI', 'A', 37)
,
('Student202', 'AI', 'A', 72)
,
('Student203', 'DEVOPS', 'E', 83)
,
('Student204', 'Cyber Security', 'A', 68)
,
('Student205', 'AI', 'D', 33)
,
('Student206', 'Cyber Security', 'D', 36)
,
('Student207', 'DEVOPS', 'D', 39)
,
('Student208', 'Data Science', 'C', 48)
,
('Student209', 'Data Science', 'E', 79)
,
('Student210', 'Data Science', 'A', 78)
,
('Student211', 'Cloud Computing', 'B', 98)
,
('Student212', 'Cyber Security', 'D', 41)
,
('Student213', 'DEVOPS', 'D', 55)
,
('Student214', 'DEVOPS', 'A', 92)
,
('Student215', 'DEVOPS', 'B', 30)
,
('Student216', 'DEVOPS', 'A', 33)
,
('Student217', 'AI', 'B', 50)
,
('Student218', 'Data Science', 'B', 91)
,
('Student219', 'Cyber Security', 'B', 79)
,
('Student220', 'Cloud Computing', 'B', 54)
,
('Student221', 'Cyber Security', 'C', 46)
,
('Student222', 'Cloud Computing', 'B', 64)
,
('Student223', 'AI', 'B', 41)
,
('Student224', 'Cloud Computing', 'B', 76)
,
('Student225', 'Data Science', 'C', 42)
,
('Student226', 'Data Science', 'A', 51)
,
('Student227', 'DEVOPS', 'C', 61)
,
('Student228', 'Data Science', 'A', 42)
,
('Student229', 'Data Science', 'D', 100)
,
('Student230', 'Data Science', 'B', 38)
,
('Student231', 'Cloud Computing', 'A', 98)
,
('Student232', 'Cloud Computing', 'D', 83)
,
('Student233', 'Cyber Security', 'E', 59)
,
('Student234', 'Data Science', 'D', 91)
,
('Student235', 'Cyber Security', 'E', 51)
,
('Student236', 'DEVOPS', 'B', 51)
,
('Student237', 'AI', 'D', 91)
,
('Student238', 'AI', 'A', 93)
,
('Student239', 'AI', 'D', 96)
,
('Student240', 'Data Science', 'D', 67)
,
('Student241', 'Cloud Computing', 'B', 86)
,
('Student242', 'AI', 'A', 100)
,
('Student243', 'Cyber Security', 'E', 92)
,
('Student244', 'Cloud Computing', 'D', 94)
,
('Student245', 'Data Science', 'A', 67)
,
('Student246', 'AI', 'D', 35)
,
('Student247', 'Cloud Computing', 'B', 87)
,
('Student248', 'Cloud Computing', 'B', 64)
,
('Student249', 'Cyber Security', 'B', 64)
,
('Student250', 'Cloud Computing', 'E', 59)
,
('Student251', 'Cloud Computing', 'D', 41)
,
('Student252', 'AI', 'B', 36)
,
('Student253', 'Cloud Computing', 'A', 96)
,
('Student254', 'DEVOPS', 'E', 33)
,
('Student255', 'DEVOPS', 'C', 82)
,
('Student256', 'Cloud Computing', 'A', 45)
,
('Student257', 'AI', 'A', 84)
,
('Student258', 'DEVOPS', 'E', 57)
,
('Student259', 'AI', 'D', 90)
,
('Student260', 'AI', 'A', 50)
,
('Student261', 'Data Science', 'A', 100)
,
('Student262', 'AI', 'A', 94)
,
('Student263', 'DEVOPS', 'A', 68)
,
('Student264', 'Cyber Security', 'C', 73)
,
('Student265', 'DEVOPS', 'A', 68)
,
('Student266', 'DEVOPS', 'B', 67)
,
('Student267', 'DEVOPS', 'A', 83)
,
('Student268', 'Cloud Computing', 'D', 64)
,
('Student269', 'AI', 'E', 95)
,
('Student270', 'Data Science', 'B', 81)
,
('Student271', 'DEVOPS', 'A', 54)
,
('Student272', 'Cyber Security', 'A', 86)
,
('Student273', 'Cyber Security', 'B', 65)
,
('Student274', 'DEVOPS', 'E', 51)
,
('Student275', 'Cloud Computing', 'E', 87)
,
('Student276', 'Cloud Computing', 'B', 85)
,
('Student277', 'Cloud Computing', 'A', 67)
,
('Student278', 'DEVOPS', 'C', 45)
,
('Student279', 'AI', 'B', 32)
,
('Student280', 'AI', 'A', 32)
,
('Student281', 'Cloud Computing', 'E', 88)
,
('Student282', 'Cloud Computing', 'D', 31)
,
('Student283', 'Data Science', 'A', 96)
,
('Student284', 'Cyber Security', 'A', 49)
,
('Student285', 'DEVOPS', 'B', 36)
,
('Student286', 'Cyber Security', 'C', 33)
,
('Student287', 'AI', 'C', 44)
,
('Student288', 'Cyber Security', 'B', 41)
,
('Student289', 'Cyber Security', 'E', 94)
,
('Student290', 'Data Science', 'E', 34)
,
('Student291', 'Cloud Computing', 'D', 36)
,
('Student292', 'Cyber Security', 'A', 63)
,
('Student293', 'DEVOPS', 'B', 33)
,
('Student294', 'Cyber Security', 'D', 63)
,
('Student295', 'Data Science', 'B', 57)
,
('Student296', 'DEVOPS', 'D', 79)
,
('Student297', 'Cloud Computing', 'C', 82)
,
('Student298', 'AI', 'D', 83)
,
('Student299', 'Data Science', 'D', 61)
,
('Student300', 'AI', 'D', 83)
,
('Student301', 'Cloud Computing', 'B', 53)
,
('Student302', 'Cloud Computing', 'B', 96)
,
('Student303', 'DEVOPS', 'B', 62)
,
('Student304', 'Cloud Computing', 'E', 72)
,
('Student305', 'DEVOPS', 'D', 47)
,
('Student306', 'Cyber Security', 'D', 89)
,
('Student307', 'Cloud Computing', 'B', 65)
,
('Student308', 'Data Science', 'D', 51)
,
('Student309', 'AI', 'B', 85)
,
('Student310', 'Data Science', 'B', 87)
,
('Student311', 'Cloud Computing', 'E', 79)
,
('Student312', 'Data Science', 'C', 99)
,
('Student313', 'AI', 'A', 37)
,
('Student314', 'Data Science', 'C', 80)
,
('Student315', 'Cyber Security', 'A', 61)
,
('Student316', 'Data Science', 'E', 86)
,
('Student317', 'DEVOPS', 'B', 98)
,
('Student318', 'Cyber Security', 'E', 54)
,
('Student319', 'DEVOPS', 'E', 73)
,
('Student320', 'Cloud Computing', 'C', 97)
,
('Student321', 'Cyber Security', 'B', 83)
,
('Student322', 'Data Science', 'E', 40)
,
('Student323', 'Cyber Security', 'B', 44)
,
('Student324', 'Cyber Security', 'E', 70)
,
('Student325', 'DEVOPS', 'A', 44)
,
('Student326', 'AI', 'A', 40)
,
('Student327', 'AI', 'B', 76)
,
('Student328', 'Data Science', 'E', 99)
,
('Student329', 'Cyber Security', 'C', 96)
,
('Student330', 'Cyber Security', 'C', 57)
,
('Student331', 'Data Science', 'E', 50)
,
('Student332', 'DEVOPS', 'E', 43)
,
('Student333', 'AI', 'D', 38)
,
('Student334', 'Cyber Security', 'B', 64)
,
('Student335', 'Data Science', 'D', 94)
,
('Student336', 'Cyber Security', 'E', 60)
,
('Student337', 'DEVOPS', 'C', 94)
,
('Student338', 'Data Science', 'B', 54)
,
('Student339', 'AI', 'A', 43)
,
('Student340', 'Cloud Computing', 'B', 71)
,
('Student341', 'AI', 'B', 95)
,
('Student342', 'Cloud Computing', 'B', 71)
,
('Student343', 'DEVOPS', 'E', 31)
,
('Student344', 'Data Science', 'D', 60)
,
('Student345', 'Data Science', 'B', 50)
,
('Student346', 'AI', 'D', 85)
,
('Student347', 'Cyber Security', 'E', 56)
,
('Student348', 'Cloud Computing', 'E', 38)
,
('Student349', 'DEVOPS', 'C', 84)
,
('Student350', 'DEVOPS', 'E', 87)
,
('Student351', 'Cyber Security', 'A', 52)
,
('Student352', 'Cyber Security', 'C', 69)
,
('Student353', 'Cyber Security', 'C', 87)
,
('Student354', 'DEVOPS', 'E', 76)
,
('Student355', 'Cyber Security', 'B', 70)
,
('Student356', 'Cyber Security', 'A', 82)
,
('Student357', 'AI', 'D', 41)
,
('Student358', 'AI', 'E', 99)
,
('Student359', 'Cyber Security', 'C', 49)
,
('Student360', 'AI', 'E', 39)
,
('Student361', 'AI', 'D', 62)
,
('Student362', 'AI', 'B', 47)
,
('Student363', 'Cloud Computing', 'C', 59)
,
('Student364', 'Cloud Computing', 'D', 37)
,
('Student365', 'DEVOPS', 'E', 32)
,
('Student366', 'Data Science', 'E', 60)
,
('Student367', 'Cyber Security', 'B', 39)
,
('Student368', 'Data Science', 'A', 35)
,
('Student369', 'AI', 'B', 75)
,
('Student370', 'Cyber Security', 'A', 30)
,
('Student371', 'Cloud Computing', 'D', 53)
,
('Student372', 'Cloud Computing', 'B', 61)
,
('Student373', 'AI', 'B', 92)
,
('Student374', 'Cyber Security', 'B', 38)
,
('Student375', 'Data Science', 'D', 46)
,
('Student376', 'DEVOPS', 'A', 79)
,
('Student377', 'DEVOPS', 'D', 97)
,
('Student378', 'Data Science', 'A', 33)
,
('Student379', 'AI', 'E', 100)
,
('Student380', 'DEVOPS', 'B', 89)
,
('Student381', 'AI', 'D', 98)
,
('Student382', 'Cloud Computing', 'E', 60)
,
('Student383', 'Data Science', 'A', 41)
,
('Student384', 'AI', 'D', 70)
,
('Student385', 'Data Science', 'C', 99)
,
('Student386', 'Cloud Computing', 'D', 86)
,
('Student387', 'AI', 'A', 58)
,
('Student388', 'Cyber Security', 'A', 44)
,
('Student389', 'Cloud Computing', 'E', 79)
,
('Student390', 'AI', 'C', 33)
,
('Student391', 'DEVOPS', 'D', 72)
,
('Student392', 'Cyber Security', 'B', 100)
,
('Student393', 'AI', 'B', 33)
,
('Student394', 'Cloud Computing', 'D', 64)
,
('Student395', 'Cloud Computing', 'D', 65)
,
('Student396', 'Data Science', 'C', 46)
,
('Student397', 'Data Science', 'E', 88)
,
('Student398', 'Data Science', 'D', 45)
,
('Student399', 'DEVOPS', 'B', 75)
,
('Student400', 'DEVOPS', 'B', 75)
,
('Student401', 'AI', 'B', 47)
,
('Student402', 'DEVOPS', 'E', 88)
,
('Student403', 'DEVOPS', 'C', 53)
,
('Student404', 'Cloud Computing', 'A', 73)
,
('Student405', 'Cyber Security', 'E', 32)
,
('Student406', 'Cyber Security', 'A', 42)
,
('Student407', 'AI', 'D', 68)
,
('Student408', 'AI', 'C', 33)
,
('Student409', 'Cyber Security', 'B', 75)
,
('Student410', 'Cloud Computing', 'D', 67)
,
('Student411', 'DEVOPS', 'B', 78)
,
('Student412', 'DEVOPS', 'A', 80)
,
('Student413', 'Data Science', 'E', 59)
,
('Student414', 'AI', 'B', 84)
,
('Student415', 'Data Science', 'C', 30)
,
('Student416', 'Data Science', 'D', 46)
,
('Student417', 'Data Science', 'D', 47)
,
('Student418', 'AI', 'D', 67)
,
('Student419', 'Data Science', 'A', 58)
,
('Student420', 'AI', 'C', 92)
,
('Student421', 'Cyber Security', 'B', 35)
,
('Student422', 'Data Science', 'D', 72)
,
('Student423', 'Data Science', 'A', 52)
,
('Student424', 'DEVOPS', 'B', 94)
,
('Student425', 'DEVOPS', 'A', 83)
,
('Student426', 'Cyber Security', 'B', 67)
,
('Student427', 'Data Science', 'C', 34)
,
('Student428', 'Data Science', 'E', 70)
,
('Student429', 'Cloud Computing', 'D', 68)
,
('Student430', 'Data Science', 'D', 61)
,
('Student431', 'AI', 'E', 93)
,
('Student432', 'DEVOPS', 'C', 32)
,
('Student433', 'AI', 'C', 100)
,
('Student434', 'Cloud Computing', 'B', 70)
,
('Student435', 'Cyber Security', 'E', 73)
,
('Student436', 'AI', 'C', 54)
,
('Student437', 'Cloud Computing', 'B', 89)
,
('Student438', 'Data Science', 'E', 43)
,
('Student439', 'Cloud Computing', 'B', 35)
,
('Student440', 'Data Science', 'A', 64)
,
('Student441', 'AI', 'B', 69)
,
('Student442', 'Data Science', 'D', 96)
,
('Student443', 'AI', 'A', 83)
,
('Student444', 'DEVOPS', 'B', 89)
,
('Student445', 'DEVOPS', 'C', 54)
,
('Student446', 'Data Science', 'D', 58)
,
('Student447', 'Data Science', 'E', 64)
,
('Student448', 'AI', 'D', 43)
,
('Student449', 'AI', 'C', 94)
,
('Student450', 'DEVOPS', 'D', 67)
,
('Student451', 'DEVOPS', 'D', 87)
,
('Student452', 'DEVOPS', 'C', 73)
,
('Student453', 'DEVOPS', 'C', 53)
,
('Student454', 'AI', 'C', 81)
,
('Student455', 'Cloud Computing', 'E', 94)
,
('Student456', 'Cyber Security', 'E', 61)
,
('Student457', 'DEVOPS', 'B', 60)
,
('Student458', 'Data Science', 'B', 84)
,
('Student459', 'AI', 'E', 58)
,
('Student460', 'Cyber Security', 'E', 92)
,
('Student461', 'DEVOPS', 'D', 39)
,
('Student462', 'Data Science', 'B', 52)
,
('Student463', 'AI', 'D', 84)
,
('Student464', 'Cloud Computing', 'D', 62)
,
('Student465', 'DEVOPS', 'C', 43)
,
('Student466', 'Data Science', 'A', 38)
,
('Student467', 'Cyber Security', 'C', 98)
,
('Student468', 'DEVOPS', 'B', 83)
,
('Student469', 'Cyber Security', 'C', 94)
,
('Student470', 'Cyber Security', 'E', 96)
,
('Student471', 'Cloud Computing', 'D', 89)
,
('Student472', 'Cyber Security', 'E', 51)
,
('Student473', 'Data Science', 'E', 48)
,
('Student474', 'Cyber Security', 'D', 96)
,
('Student475', 'DEVOPS', 'B', 98)
,
('Student476', 'Data Science', 'D', 65)
,
('Student477', 'Cloud Computing', 'C', 50)
,
('Student478', 'Data Science', 'C', 81)
,
('Student479', 'Cloud Computing', 'D', 75)
,
('Student480', 'Cloud Computing', 'A', 56)
,
('Student481', 'DEVOPS', 'B', 59)
,
('Student482', 'Data Science', 'E', 86)
,
('Student483', 'DEVOPS', 'A', 80)
,
('Student484', 'Cyber Security', 'C', 55)
,
('Student485', 'DEVOPS', 'C', 77)
,
('Student486', 'AI', 'C', 58)
,
('Student487', 'Cyber Security', 'D', 95)
,
('Student488', 'Cyber Security', 'B', 98)
,
('Student489', 'AI', 'B', 91)
,
('Student490', 'Cloud Computing', 'E', 65)
,
('Student491', 'Cyber Security', 'C', 35)
,
('Student492', 'DEVOPS', 'E', 41)
,
('Student493', 'Cloud Computing', 'D', 85)
,
('Student494', 'Data Science', 'D', 75)
,
('Student495', 'Cyber Security', 'B', 48)
,
('Student496', 'Cloud Computing', 'A', 90)
,
('Student497', 'Data Science', 'D', 40)
,
('Student498', 'DEVOPS', 'B', 72)
,
('Student499', 'Cyber Security', 'D', 47)
,
('Student500', 'DEVOPS', 'E', 98)
]

cursor.executemany(sql_query, values)
connection.commit()

# Display the records
data=cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

if connection:
    connection.close()