import React from 'react';
import '../css/Header.css';

const Header = () => {
    return (
        <div className="header_all">
            <div className="header_title header_child">
                집 찾기
            </div>
            <div className="header_list header_child">
                <div className="header_subList header_home">집 사기</div>
                <div className="header_subList header_home">집 팔기</div>
                <div className="header_subList header_login">로그인</div>
            </div>
        </div>
    );
};

export default Header;