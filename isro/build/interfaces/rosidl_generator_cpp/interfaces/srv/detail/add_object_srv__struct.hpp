// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/AddObjectSrv.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__srv__AddObjectSrv_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__AddObjectSrv_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddObjectSrv_Request_
{
  using Type = AddObjectSrv_Request_<ContainerAllocator>;

  explicit AddObjectSrv_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->tag = 0;
    }
  }

  explicit AddObjectSrv_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->tag = 0;
    }
  }

  // field types and members
  using _pose_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _pose_type pose;
  using _tag_type =
    int8_t;
  _tag_type tag;

  // setters for named parameter idiom
  Type & set__pose(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }
  Type & set__tag(
    const int8_t & _arg)
  {
    this->tag = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::AddObjectSrv_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::AddObjectSrv_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::AddObjectSrv_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::AddObjectSrv_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__AddObjectSrv_Request
    std::shared_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__AddObjectSrv_Request
    std::shared_ptr<interfaces::srv::AddObjectSrv_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddObjectSrv_Request_ & other) const
  {
    if (this->pose != other.pose) {
      return false;
    }
    if (this->tag != other.tag) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddObjectSrv_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddObjectSrv_Request_

// alias to use template instance with default allocator
using AddObjectSrv_Request =
  interfaces::srv::AddObjectSrv_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__AddObjectSrv_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__AddObjectSrv_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AddObjectSrv_Response_
{
  using Type = AddObjectSrv_Response_<ContainerAllocator>;

  explicit AddObjectSrv_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = 0;
    }
  }

  explicit AddObjectSrv_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = 0;
    }
  }

  // field types and members
  using _success_type =
    int8_t;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const int8_t & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::AddObjectSrv_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::AddObjectSrv_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::AddObjectSrv_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::AddObjectSrv_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__AddObjectSrv_Response
    std::shared_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__AddObjectSrv_Response
    std::shared_ptr<interfaces::srv::AddObjectSrv_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AddObjectSrv_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const AddObjectSrv_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AddObjectSrv_Response_

// alias to use template instance with default allocator
using AddObjectSrv_Response =
  interfaces::srv::AddObjectSrv_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct AddObjectSrv
{
  using Request = interfaces::srv::AddObjectSrv_Request;
  using Response = interfaces::srv::AddObjectSrv_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__ADD_OBJECT_SRV__STRUCT_HPP_
