# Backend API Documentation - PBL6 Expense Tracker

## 1. Giới thiệu tổng quan
Hệ thống máy chủ backend xây dựng trên nền tảng **Node.js**, chịu trách nhiệm cung cấp RESTful API cho ứng dụng di động Flutter. Backend đảm nhận xử lý logic nghiệp vụ, quản lý phân quyền, lưu trữ dữ liệu tài chính trên Supabase PostgreSQL, upload hình ảnh lên Supabase Storage và điều phối xử lý trích xuất dữ liệu hóa đơn (OCR/AI).

## 2. Công nghệ sử dụng
- **Runtime:** Node.js (v18+ / v20+)
- **Language / Framework:** TypeScript + Express.js (hoặc NestJS)
- **Database:** Supabase PostgreSQL (truy vấn qua Prisma ORM / Supabase-JS SDK)
- **File Storage:** Supabase Storage (lưu trữ ảnh hóa đơn gốc, avatar)
- **Authentication:** JWT (JSON Web Token) / Supabase Auth
- **File Upload Middleware:** Multer