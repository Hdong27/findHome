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
	// �⺻Ű
	@Column
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer unum;
	
	// ���̵�
	@Column(unique = true)
	private String uid;
	
	// �н�����
	@Column
	private String upassword;
	
	// �̸�
	@Column
	private String uname;
	
	// �г���
	@Column
	private String unickname;
	
	// �ڵ��� ��ȣ
	@Column
	private String uphone;
	
	// ȸ������ �ð�
	@Column
	@CreationTimestamp
	private LocalDate utime;
	
	// ȸ��Ż�� ����
	@Column
	private Boolean uisDel = false;
}
