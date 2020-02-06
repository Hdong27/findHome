package com.example.findHome.user.dto;

import java.time.LocalDate;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.CreationTimestamp;

import lombok.Data;

@Data
@Entity
@Table(name = "users")
public class User {
	// 기본키
	@Column
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer unum;
	
	// 아이디
	@Column(unique = true)
	private String uid;
	
	// 패스워드
	@Column
	private String upassword;
	
	// 이름
	@Column
	private String uname;
	
	// 닉네임
	@Column
	private String unickname;
	
	// 핸드폰 번호
	@Column
	private String uphone;
	
	// 회원가입 시간
	@Column
	@CreationTimestamp
	private LocalDate utime;
	
	// 회원탈퇴 여부
	@Column
	private Boolean uisDel = false;
}
