// Generated by gencpp from file pub_sub_topic_communication/Person.msg
// DO NOT EDIT!


#ifndef PUB_SUB_TOPIC_COMMUNICATION_MESSAGE_PERSON_H
#define PUB_SUB_TOPIC_COMMUNICATION_MESSAGE_PERSON_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pub_sub_topic_communication
{
template <class ContainerAllocator>
struct Person_
{
  typedef Person_<ContainerAllocator> Type;

  Person_()
    : name()
    , age(0)
    , height(0.0)  {
    }
  Person_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , age(0)
    , height(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef int32_t _age_type;
  _age_type age;

   typedef float _height_type;
  _height_type height;





  typedef boost::shared_ptr< ::pub_sub_topic_communication::Person_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pub_sub_topic_communication::Person_<ContainerAllocator> const> ConstPtr;

}; // struct Person_

typedef ::pub_sub_topic_communication::Person_<std::allocator<void> > Person;

typedef boost::shared_ptr< ::pub_sub_topic_communication::Person > PersonPtr;
typedef boost::shared_ptr< ::pub_sub_topic_communication::Person const> PersonConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pub_sub_topic_communication::Person_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pub_sub_topic_communication::Person_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pub_sub_topic_communication::Person_<ContainerAllocator1> & lhs, const ::pub_sub_topic_communication::Person_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.age == rhs.age &&
    lhs.height == rhs.height;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pub_sub_topic_communication::Person_<ContainerAllocator1> & lhs, const ::pub_sub_topic_communication::Person_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pub_sub_topic_communication

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pub_sub_topic_communication::Person_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pub_sub_topic_communication::Person_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pub_sub_topic_communication::Person_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
{
  static const char* value()
  {
    return "0478132ca0c3bd1c734b5491000dabb1";
  }

  static const char* value(const ::pub_sub_topic_communication::Person_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x0478132ca0c3bd1cULL;
  static const uint64_t static_value2 = 0x734b5491000dabb1ULL;
};

template<class ContainerAllocator>
struct DataType< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pub_sub_topic_communication/Person";
  }

  static const char* value(const ::pub_sub_topic_communication::Person_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string name\n"
"int32 age\n"
"float32 height\n"
;
  }

  static const char* value(const ::pub_sub_topic_communication::Person_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.age);
      stream.next(m.height);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Person_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pub_sub_topic_communication::Person_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pub_sub_topic_communication::Person_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "age: ";
    Printer<int32_t>::stream(s, indent + "  ", v.age);
    s << indent << "height: ";
    Printer<float>::stream(s, indent + "  ", v.height);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PUB_SUB_TOPIC_COMMUNICATION_MESSAGE_PERSON_H
