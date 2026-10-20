-- ==============================================================================
-- BÀI TẬP: THÊM DỮ LIỆU VÀO TRONG BẢNG BẰNG CÂU LỆNH INSERT INTO
-- Cơ sở dữ liệu: QuanLySinhVien
-- Sinh viên thực hiện: DTC245200413
-- Repository: https://github.com/dtc245200413-cmyk/jwbd-2023-sql-student-management-insert-into
-- Tham khảo: https://github.com/codegym-vn/jwbd-2023-sql-student-management-insert-into (branch dev)
-- ==============================================================================

-- Bước 1: Sử dụng câu lệnh USE QuanLySinhVien để thao tác với cơ sở dữ liệu
USE QuanLySinhVien;

-- Bước 2: Thêm lần lượt các bản ghi vào trong bảng Class
INSERT INTO Class
VALUES (1, 'A1', '2008-12-20', 1);

INSERT INTO Class
VALUES (2, 'A2', '2008-12-22', 1);

INSERT INTO Class
VALUES (3, 'B3', current_date, 0);

-- Bước 3: Thêm dữ liệu vào trong bảng Student
-- Chú ý: Học sinh 'Hoa' không có số điện thoại (Phone) nên ta chỉ định danh sách cột bỏ qua Phone (nhận giá trị NULL)
INSERT INTO Student (StudentName, Address, Phone, Status, ClassId)
VALUES ('Hung', 'Ha Noi', '0912113113', 1, 1);

INSERT INTO Student (StudentName, Address, Status, ClassId)
VALUES ('Hoa', 'Hai phong', 1, 1);

INSERT INTO Student (StudentName, Address, Phone, Status, ClassId)
VALUES ('Manh', 'HCM', '0123123123', 0, 2);

-- Bước 4: Thêm dữ liệu nhiều dòng cùng lúc (Batch Insert) vào trong bảng Subject
INSERT INTO Subject
VALUES (1, 'CF', 5, 1),
       (2, 'C', 6, 1),
       (3, 'HDJ', 5, 1),
       (4, 'RDBMS', 10, 1);

-- Bước 5: Thêm dữ liệu vào trong bảng Mark
INSERT INTO Mark (SubId, StudentId, Mark, ExamTimes)
VALUES (1, 1, 8, 1),
       (1, 2, 10, 2),
       (2, 1, 12, 1);

-- ==============================================================================
-- TRUY VẤN KIỂM CHỨNG DỮ LIỆU ĐÃ THÊM THÀNH CÔNG
-- ==============================================================================

-- 1. Kiểm tra bảng Class
SELECT * FROM Class;

-- 2. Kiểm tra bảng Student
SELECT * FROM Student;

-- 3. Kiểm tra bảng Subject
SELECT * FROM Subject;

-- 4. Kiểm tra bảng Mark
SELECT * FROM Mark;

-- 5. Xem bảng điểm chi tiết kèm tên sinh viên, tên lớp và tên môn học
SELECT 
    m.MarkId,
    s.StudentName,
    c.ClassName,
    sub.SubName,
    m.Mark,
    m.ExamTimes
FROM Mark m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Class c ON s.ClassID = c.ClassID
JOIN Subject sub ON m.SubID = sub.SubID;
