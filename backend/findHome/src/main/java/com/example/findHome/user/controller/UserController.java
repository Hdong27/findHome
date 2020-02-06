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
		log.debug("test 호출");
		return new ResponseEntity<String>("통신 가능", HttpStatus.OK);
	}
	
	// 회원가입
	@PostMapping("/user/1")
	public ResponseEntity<Boolean> signUp(@RequestBody User user) {
		log.debug(user.getUname() + "님의 회원가입 요청");
		return new ResponseEntity<Boolean>(userService.signUp(user), HttpStatus.OK);
	}
	
	// 아이디 중복 확인
	@GetMapping("/user/2")
	public ResponseEntity<Boolean> isPossibleId(@RequestBody User user) {
		log.debug(user.getUid() + " <-- 아이디 중복 확인");
		return new ResponseEntity<Boolean>(userService.isPossibleId(user.getUid()), HttpStatus.OK);
	}
	
	// 로그인 확인
	@PostMapping("/user/3")
	public ResponseEntity<User> login(@RequestBody User user) {
		log.debug(user.getUid() + " 로그인 요청");
		return new ResponseEntity<User>(userService.login(user), HttpStatus.OK);
		// unum == 0 일경우 로그인 실패!
	}
	
	// 회원정보 변경
	@PutMapping("/user/4")
	public ResponseEntity<User> updateUser(@RequestBody User user) {
		log.debug(user.getUid() + "의 회원정보 변경 요청");
		return new ResponseEntity<User>(userService.updateUser(user), HttpStatus.OK);
	}
	
	// 회원탈퇴 : 탈퇴 여부에 true
	@PutMapping("/user/5")
	public ResponseEntity<Boolean> deleteUser(@RequestBody User user) {
		log.debug(user.getUid() + "의 회원탈퇴 요청");
		return new ResponseEntity<Boolean>(userService.deleteUser(user), HttpStatus.OK);
	}
}
