package com.example.findHome.user.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.findHome.user.controller.SecurityUtil;
import com.example.findHome.user.dto.User;
import com.example.findHome.user.repository.UserRepository;

@Service
public class UserServiceImpl implements UserService {
	@Autowired
	private UserRepository userRepository;
	
	// 회원가입
	@Override
	public boolean signUp(User user) {
		// 비밀번호 암호화
		user.setUpassword(new SecurityUtil().encodeSHA256(user.getUpassword()));
		userRepository.save(user);
		// 추후에 예외상황에 대해 try...catch문 추가
		return true;
	}

	// 아이디 중복확인
	@Override
	public boolean isPossibleId(String uid) {
		Optional<User> maybeUser = userRepository.findByUid(uid);
		if(maybeUser.isPresent()) {
			return false;
		} else {
			return true;
		}
	}

	// 로그인
	@Override
	public User login(User user) {
		User failUser = new User();
		failUser.setUnum(0);
		Optional<User> maybeUser = userRepository.findByUid(user.getUid());
		if(maybeUser.isPresent() && !maybeUser.get().getUisDel()) {
			if(maybeUser.get().getUpassword().equals(new SecurityUtil().encodeSHA256(user.getUpassword()))) {
				return maybeUser.get();
			}
		}
		return failUser;
	}

	// 회원정보 변경
	@Override
	public User updateUser(User user) {
		userRepository.update(user);
		return userRepository.findById(user.getUnum()).get();
	}

	// 회원탈퇴
	@Override
	public boolean deleteUser(User user) {
		userRepository.deleteUser(user);
		return true;
	}
}
