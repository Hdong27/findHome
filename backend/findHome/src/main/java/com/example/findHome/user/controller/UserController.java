package com.example.findHome.user.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.example.findHome.user.dto.User;
import com.example.findHome.user.service.UserService;

import lombok.extern.slf4j.Slf4j;


@Controller
@Slf4j
public class UserController {
	@Autowired
	private UserService userService;
	
	// test
	@GetMapping("/test")
	public ResponseEntity<String> test(HttpServletRequest request) {
		log.debug("test ȣ��");
		return new ResponseEntity<String>("��� ����", HttpStatus.OK);
	}
	
	// ȸ������
	@PostMapping("/user/1")
	public ResponseEntity<Boolean> signUp(@RequestBody User user) {
		log.debug(user.getUname() + "���� ȸ������ ��û");
		return new ResponseEntity<Boolean>(userService.signUp(user), HttpStatus.OK);
	}
	
	// ���̵� �ߺ� Ȯ��
	@GetMapping("/user/2")
	public ResponseEntity<Boolean> isPossibleId(@RequestBody User user) {
		log.debug(user.getUid() + " <-- ���̵� �ߺ� Ȯ��");
		return new ResponseEntity<Boolean>(userService.isPossibleId(user.getUid()), HttpStatus.OK);
	}
	
	// �α��� Ȯ��
	@PostMapping("/user/3")
	public ResponseEntity<User> login(@RequestBody User user) {
		log.debug(user.getUid() + " �α��� ��û");
		return new ResponseEntity<User>(userService.login(user), HttpStatus.OK);
		// unum == 0 �ϰ�� �α��� ����!
	}
	
	// ȸ������ ����
	@PutMapping("/user/4")
	public ResponseEntity<User> updateUser(@RequestBody User user) {
		log.debug(user.getUid() + "�� ȸ������ ���� ��û");
		return new ResponseEntity<User>(userService.updateUser(user), HttpStatus.OK);
	}
	
	// ȸ��Ż�� : Ż�� ���ο� true
	@PutMapping("/user/5")
	public ResponseEntity<Boolean> deleteUser(@RequestBody User user) {
		log.debug(user.getUid() + "�� ȸ��Ż�� ��û");
		return new ResponseEntity<Boolean>(userService.deleteUser(user), HttpStatus.OK);
	}
}
