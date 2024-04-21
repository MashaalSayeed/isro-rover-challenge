// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/AddObjectSrv.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__TRAITS_HPP_

#include "interfaces/srv/detail/add_object_srv__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::AddObjectSrv_Request>()
{
  return "interfaces::srv::AddObjectSrv_Request";
}

template<>
inline const char * name<interfaces::srv::AddObjectSrv_Request>()
{
  return "interfaces/srv/AddObjectSrv_Request";
}

template<>
struct has_fixed_size<interfaces::srv::AddObjectSrv_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct has_bounded_size<interfaces::srv::AddObjectSrv_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct is_message<interfaces::srv::AddObjectSrv_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::AddObjectSrv_Response>()
{
  return "interfaces::srv::AddObjectSrv_Response";
}

template<>
inline const char * name<interfaces::srv::AddObjectSrv_Response>()
{
  return "interfaces/srv/AddObjectSrv_Response";
}

template<>
struct has_fixed_size<interfaces::srv::AddObjectSrv_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::AddObjectSrv_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::AddObjectSrv_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::AddObjectSrv>()
{
  return "interfaces::srv::AddObjectSrv";
}

template<>
inline const char * name<interfaces::srv::AddObjectSrv>()
{
  return "interfaces/srv/AddObjectSrv";
}

template<>
struct has_fixed_size<interfaces::srv::AddObjectSrv>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::AddObjectSrv_Request>::value &&
    has_fixed_size<interfaces::srv::AddObjectSrv_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::AddObjectSrv>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::AddObjectSrv_Request>::value &&
    has_bounded_size<interfaces::srv::AddObjectSrv_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::AddObjectSrv>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::AddObjectSrv_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::AddObjectSrv_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__TRAITS_HPP_
