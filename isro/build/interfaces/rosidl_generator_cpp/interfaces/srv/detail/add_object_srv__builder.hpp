// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/AddObjectSrv.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__BUILDER_HPP_

#include "interfaces/srv/detail/add_object_srv__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_AddObjectSrv_Request_tag
{
public:
  explicit Init_AddObjectSrv_Request_tag(::interfaces::srv::AddObjectSrv_Request & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::AddObjectSrv_Request tag(::interfaces::srv::AddObjectSrv_Request::_tag_type arg)
  {
    msg_.tag = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::AddObjectSrv_Request msg_;
};

class Init_AddObjectSrv_Request_pose
{
public:
  Init_AddObjectSrv_Request_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddObjectSrv_Request_tag pose(::interfaces::srv::AddObjectSrv_Request::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_AddObjectSrv_Request_tag(msg_);
  }

private:
  ::interfaces::srv::AddObjectSrv_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::AddObjectSrv_Request>()
{
  return interfaces::srv::builder::Init_AddObjectSrv_Request_pose();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_AddObjectSrv_Response_success
{
public:
  Init_AddObjectSrv_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::AddObjectSrv_Response success(::interfaces::srv::AddObjectSrv_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::AddObjectSrv_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::AddObjectSrv_Response>()
{
  return interfaces::srv::builder::Init_AddObjectSrv_Response_success();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__BUILDER_HPP_
