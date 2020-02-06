package com.example.findHome.user.service;

import com.example.findHome.user.dto.User;

public interface UserService {
	// ȸ������
	public boolean signUp(User user);
	
	// ���̵� �ߺ�Ȯ��
	public boolean isPossibleId(String uid);
	
	// �α���
	public User login(User user);
	
	// ȸ������ ����
	public User updateUser(User user);
	
	// ȸ��Ż��
	public boolean deleteUser(User user);
}
