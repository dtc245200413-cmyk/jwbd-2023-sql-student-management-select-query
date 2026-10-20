-- ==============================================================================
-- BÀI TẬP: TRUY VẤN DỮ LIỆU TỪ NHIỀU BẢNG TRONG MYSQL (QuanLySinhVien)
-- Sinh viên thực hiện: DTC245200413
-- Repository: https://github.com/dtc245200413-cmyk/jwbd-2023-sql-student-management-select-query
-- Tham khảo: https://github.com/codegym-vn/jwbd-2023-sql-student-management-select-query (branch dev)
-- ==============================================================================

-- Bước 1: Sử dụng cơ sở dữ liệu QuanLySinhVien
USE QuanLySinhVien;

-- Bước 2: Hiển thị danh sách tất cả các học viên
SELECT *
FROM Student;

-- Bước 3: Hiển thị danh sách các học viên đang theo học (Status = true hoặc Status = 1)
SELECT *
FROM Student
WHERE Status = true;

-- Bước 4: Hiển thị danh sách các môn học có thời gian học / số tín chỉ nhỏ hơn 10 (Credit < 10)
SELECT *
FROM Subject
WHERE Credit < 10;

-- Bước 5: Sử dụng câu lệnh JOIN và WHERE để hiển thị danh sách học viên lớp A1
SELECT S.StudentId, S.StudentName, C.ClassName
FROM Student S 
JOIN Class C ON S.ClassId = C.ClassID
WHERE C.ClassName = 'A1';

-- Bước 6: Hiển thị điểm môn CF của các học viên
SELECT S.StudentId, S.StudentName, Sub.SubName, M.Mark
FROM Student S 
JOIN Mark M ON S.StudentId = M.StudentId 
JOIN Subject Sub ON M.SubId = Sub.SubId
WHERE Sub.SubName = 'CF';
