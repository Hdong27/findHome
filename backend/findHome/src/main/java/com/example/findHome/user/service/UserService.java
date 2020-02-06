package com.example.findHome.user.service;

import com.example.findHome.user.dto.User;

public interface UserService {
	// 회원가입
	public boolean signUp(User user);
	
	// 아이디 중복확인
	public boolean isPossibleId(String uid);
	
	// 로그인
	public User login(User user);
	
	// 회원정보 변경
	public User updateUser(User user);
	
	// 회원탈퇴
	public boolean deleteUser(User user);
}
