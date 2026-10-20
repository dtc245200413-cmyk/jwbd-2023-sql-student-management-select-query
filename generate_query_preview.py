import os
import shutil
import subprocess
import tempfile

svg_content = """<svg width="1280" height="840" viewBox="0 0 1280 840" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border-radius: 12px;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <style>
    .tbl-title { font-size: 13px; font-weight: 800; fill: #ffffff; }
    .sql-code { font-size: 11px; font-family: monospace; fill: #475569; }
    .th { font-size: 11px; font-weight: 800; fill: #1e293b; background: #f8fafc; }
    .td { font-size: 11px; fill: #334155; }
    .td-pk { font-size: 11px; font-weight: 800; fill: #b91c1c; }
    .td-hl { font-size: 11px; font-weight: 700; fill: #16a34a; }
  </style>

  <!-- Title Banner -->
  <rect x="30" y="20" width="1220" height="48" rx="8" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5" />
  <text x="640" y="50" font-size="16" font-weight="800" fill="#1e40af" text-anchor="middle">
    KẾT QUẢ THỰC THI CÁC CÂU TRUY VẤN DỮ LIỆU (SELECT QUERY RESULTS)
  </text>

  <!-- QUERY 1: All Students -->
  <g transform="translate(60, 95)" filter="url(#shadow)">
    <rect width="550" height="215" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 542,0 Q 550,0 550,8 L 550,30 L 0,30 Z" fill="#1e40af" />
    <text x="14" y="20" class="tbl-title">1. Hiển thị danh sách tất cả các học viên</text>
    <rect x="10" y="38" width="530" height="22" fill="#f8fafc" rx="4" stroke="#e2e8f0" />
    <text x="18" y="53" class="sql-code">SELECT * FROM Student;</text>

    <!-- Header -->
    <rect x="10" y="68" width="530" height="24" fill="#f1f5f9" rx="3" />
    <text x="20" y="84" class="th">StudentId</text>
    <text x="90" y="84" class="th">StudentName</text>
    <text x="185" y="84" class="th">Address</text>
    <text x="280" y="84" class="th">Phone</text>
    <text x="385" y="84" class="th">Status</text>
    <text x="465" y="84" class="th">ClassId</text>

    <!-- Rows -->
    <line x1="10" y1="120" x2="540" y2="120" stroke="#f1f5f9" />
    <text x="20" y="110" class="td-pk">1</text>
    <text x="90" y="110" class="td">Hung</text>
    <text x="185" y="110" class="td">Ha Noi</text>
    <text x="280" y="110" class="td">0912113113</text>
    <text x="385" y="110" class="td">1</text>
    <text x="465" y="110" class="td">1</text>

    <line x1="10" y1="150" x2="540" y2="150" stroke="#f1f5f9" />
    <text x="20" y="140" class="td-pk">2</text>
    <text x="90" y="140" class="td">Hoa</text>
    <text x="185" y="140" class="td">Hai phong</text>
    <text x="280" y="140" class="td" fill="#94a3b8">NULL</text>
    <text x="385" y="140" class="td">1</text>
    <text x="465" y="140" class="td">1</text>

    <text x="20" y="170" class="td-pk">3</text>
    <text x="90" y="170" class="td">Manh</text>
    <text x="185" y="170" class="td">HCM</text>
    <text x="280" y="170" class="td">0123123123</text>
    <text x="385" y="170" class="td">0</text>
    <text x="465" y="170" class="td">2</text>
  </g>

  <!-- QUERY 2: Active Students -->
  <g transform="translate(670, 95)" filter="url(#shadow)">
    <rect width="550" height="215" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 542,0 Q 550,0 550,8 L 550,30 L 0,30 Z" fill="#4338ca" />
    <text x="14" y="20" class="tbl-title">2. Hiển thị học viên đang theo học (Status = true)</text>
    <rect x="10" y="38" width="530" height="22" fill="#f8fafc" rx="4" stroke="#e2e8f0" />
    <text x="18" y="53" class="sql-code">SELECT * FROM Student WHERE Status = true;</text>

    <!-- Header -->
    <rect x="10" y="68" width="530" height="24" fill="#f1f5f9" rx="3" />
    <text x="20" y="84" class="th">StudentId</text>
    <text x="90" y="84" class="th">StudentName</text>
    <text x="185" y="84" class="th">Address</text>
    <text x="280" y="84" class="th">Phone</text>
    <text x="385" y="84" class="th">Status</text>
    <text x="465" y="84" class="th">ClassId</text>

    <!-- Rows -->
    <line x1="10" y1="120" x2="540" y2="120" stroke="#f1f5f9" />
    <text x="20" y="110" class="td-pk">1</text>
    <text x="90" y="110" class="td">Hung</text>
    <text x="185" y="110" class="td">Ha Noi</text>
    <text x="280" y="110" class="td">0912113113</text>
    <text x="385" y="110" class="td-hl">1 (Đang học)</text>
    <text x="465" y="110" class="td">1</text>

    <text x="20" y="140" class="td-pk">2</text>
    <text x="90" y="140" class="td">Hoa</text>
    <text x="185" y="140" class="td">Hai phong</text>
    <text x="280" y="140" class="td" fill="#94a3b8">NULL</text>
    <text x="385" y="140" class="td-hl">1 (Đang học)</text>
    <text x="465" y="140" class="td">1</text>
  </g>

  <!-- QUERY 3: Subject Credit < 10 -->
  <g transform="translate(60, 335)" filter="url(#shadow)">
    <rect width="550" height="220" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 542,0 Q 550,0 550,8 L 550,30 L 0,30 Z" fill="#0f766e" />
    <text x="14" y="20" class="tbl-title">3. Danh sách môn học có thời gian/tín chỉ &lt; 10</text>
    <rect x="10" y="38" width="530" height="22" fill="#f8fafc" rx="4" stroke="#e2e8f0" />
    <text x="18" y="53" class="sql-code">SELECT * FROM Subject WHERE Credit &lt; 10;</text>

    <rect x="10" y="68" width="530" height="24" fill="#f1f5f9" rx="3" />
    <text x="30" y="84" class="th">SubId (PK)</text>
    <text x="160" y="84" class="th">SubName</text>
    <text x="310" y="84" class="th">Credit (&lt; 10)</text>
    <text x="450" y="84" class="th">Status</text>

    <!-- Rows -->
    <line x1="10" y1="120" x2="540" y2="120" stroke="#f1f5f9" />
    <text x="30" y="110" class="td-pk">1</text>
    <text x="160" y="110" class="td">CF</text>
    <text x="310" y="110" class="td-hl">5 tín chỉ</text>
    <text x="450" y="110" class="td">1</text>

    <line x1="10" y1="150" x2="540" y2="150" stroke="#f1f5f9" />
    <text x="30" y="140" class="td-pk">2</text>
    <text x="160" y="140" class="td">C</text>
    <text x="310" y="140" class="td-hl">6 tín chỉ</text>
    <text x="450" y="140" class="td">1</text>

    <text x="30" y="170" class="td-pk">3</text>
    <text x="160" y="170" class="td">HDJ</text>
    <text x="310" y="170" class="td-hl">5 tín chỉ</text>
    <text x="450" y="170" class="td">1</text>
  </g>

  <!-- QUERY 4: Students in Class A1 -->
  <g transform="translate(670, 335)" filter="url(#shadow)">
    <rect width="550" height="220" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 542,0 Q 550,0 550,8 L 550,30 L 0,30 Z" fill="#b45309" />
    <text x="14" y="20" class="tbl-title">4. Danh sách học viên lớp A1 (JOIN Class)</text>
    <rect x="10" y="38" width="530" height="34" fill="#f8fafc" rx="4" stroke="#e2e8f0" />
    <text x="18" y="52" class="sql-code">SELECT S.StudentId, S.StudentName, C.ClassName</text>
    <text x="18" y="66" class="sql-code">FROM Student S JOIN Class C ON S.ClassId = C.ClassID WHERE C.ClassName = 'A1';</text>

    <rect x="10" y="80" width="530" height="24" fill="#f1f5f9" rx="3" />
    <text x="30" y="96" class="th">StudentId</text>
    <text x="210" y="96" class="th">StudentName</text>
    <text x="410" y="96" class="th">ClassName</text>

    <!-- Rows -->
    <line x1="10" y1="130" x2="540" y2="130" stroke="#f1f5f9" />
    <text x="30" y="122" class="td-pk">1</text>
    <text x="210" y="122" class="td">Hung</text>
    <text x="410" y="122" class="td-hl">A1</text>

    <text x="30" y="152" class="td-pk">2</text>
    <text x="210" y="152" class="td">Hoa</text>
    <text x="410" y="152" class="td-hl">A1</text>
  </g>

  <!-- QUERY 5: CF Marks -->
  <g transform="translate(60, 580)" filter="url(#shadow)">
    <rect width="1160" height="195" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 1152,0 Q 1160,0 1160,8 L 1160,30 L 0,30 Z" fill="#c2410c" />
    <text x="16" y="20" class="tbl-title">5. Hiển thị điểm môn CF của các học viên (JOIN 3 bảng: Student, Mark, Subject)</text>
    
    <rect x="12" y="38" width="1136" height="34" fill="#f8fafc" rx="4" stroke="#e2e8f0" />
    <text x="20" y="52" class="sql-code">SELECT S.StudentId, S.StudentName, Sub.SubName, M.Mark</text>
    <text x="20" y="66" class="sql-code">FROM Student S JOIN Mark M ON S.StudentId = M.StudentId JOIN Subject Sub ON M.SubId = Sub.SubId WHERE Sub.SubName = 'CF';</text>

    <rect x="12" y="80" width="1136" height="24" fill="#f1f5f9" rx="3" />
    <text x="40" y="96" class="th">StudentId</text>
    <text x="250" y="96" class="th">StudentName</text>
    <text x="550" y="96" class="th">SubName</text>
    <text x="850" y="96" class="th">Mark</text>

    <!-- Rows -->
    <line x1="12" y1="130" x2="1148" y2="130" stroke="#f1f5f9" />
    <text x="40" y="122" class="td-pk">1</text>
    <text x="250" y="122" class="td">Hung</text>
    <text x="550" y="122" class="td">CF</text>
    <text x="850" y="122" class="td-hl">8.0 điểm</text>

    <text x="40" y="152" class="td-pk">2</text>
    <text x="250" y="152" class="td">Hoa</text>
    <text x="550" y="152" class="td">CF</text>
    <text x="850" y="152" class="td-hl">10.0 điểm</text>
  </g>
</svg>
"""

base_dir = r"C:\Users\Admin\.gemini\antigravity-ide\scratch\jwbd-2023-sql-student-management-select-query"
assets_dir = os.path.join(base_dir, "assets")

svg_path = os.path.join(assets_dir, "query_results_preview.svg")
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Kết quả truy vấn CSDL QuanLySinhVien</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 30px;
    }}
    .card {{
      background: #ffffff;
      border-radius: 20px;
      padding: 24px 28px 32px 28px;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08);
      border: 1px solid #cbd5e1;
    }}
  </style>
</head>
<body>
  <div class="card">
    {svg_content}
  </div>
</body>
</html>
"""

html_path = os.path.join(assets_dir, "index.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = tempfile.gettempdir()
temp_png = os.path.join(temp_dir, "query_results_preview.png")
dest_png = os.path.join(assets_dir, "query_results_preview.png")

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--window-size=1400,980",
    f"--screenshot={temp_png}",
    "file:///" + html_path.replace("\\", "/")
]

subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(temp_png):
    shutil.copy2(temp_png, dest_png)
    print("Query preview PNG rendered successfully to", dest_png)
else:
    print("Error rendering PNG")
