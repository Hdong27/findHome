package com.example.findHome.user.repository;

import java.util.Optional;

import javax.transaction.Transactional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.example.findHome.user.dto.User;

public interface UserRepository extends JpaRepository<User, Integer>{
	public Optional<User> findByUid(String uid);
	
	@Modifying
	@Query(value="update User u set u.uname = :#{#user.uname}, u.unickname = :#{#user.unickname}, u.uphone = :#{#user.uphone} WHERE u.unum = :#{#user.unum}", nativeQuery=false)
	@Transactional
	void update(@Param("user") User user);
	
	@Modifying
	@Query(value="update User u set u.uisDel = true WHERE u.unum = :#{#user.unum}", nativeQuery = false)
	@Transactional
	void deleteUser(@Param("user") User user);
}
