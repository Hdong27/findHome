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
	
	// ȸ������
	@Override
	public boolean signUp(User user) {
		// ��й�ȣ ��ȣȭ
		user.setUpassword(new SecurityUtil().encodeSHA256(user.getUpassword()));
		userRepository.save(user);
		// ���Ŀ� ���ܻ�Ȳ�� ���� try...catch�� �߰�
		return true;
	}

	// ���̵� �ߺ�Ȯ��
	@Override
	public boolean isPossibleId(String uid) {
		Optional<User> maybeUser = userRepository.findByUid(uid);
		if(maybeUser.isPresent()) {
			return false;
		} else {
			return true;
		}
	}

	// �α���
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

	// ȸ������ ����
	@Override
	public User updateUser(User user) {
		userRepository.update(user);
		return userRepository.findById(user.getUnum()).get();
	}

	// ȸ��Ż��
	@Override
	public boolean deleteUser(User user) {
		userRepository.deleteUser(user);
		return true;
	}
}
