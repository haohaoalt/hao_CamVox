// Generated by gencpp from file inertial_sense/RTKRel.msg
// DO NOT EDIT!


#ifndef INERTIAL_SENSE_MESSAGE_RTKREL_H
#define INERTIAL_SENSE_MESSAGE_RTKREL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Vector3.h>

namespace inertial_sense
{
template <class ContainerAllocator>
struct RTKRel_
{
  typedef RTKRel_<ContainerAllocator> Type;

  RTKRel_()
    : header()
    , differential_age(0.0)
    , ar_ratio(0.0)
    , vector_base_to_rover()
    , distance_base_to_rover(0.0)
    , heading_base_to_rover(0.0)  {
    }
  RTKRel_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , differential_age(0.0)
    , ar_ratio(0.0)
    , vector_base_to_rover(_alloc)
    , distance_base_to_rover(0.0)
    , heading_base_to_rover(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _differential_age_type;
  _differential_age_type differential_age;

   typedef float _ar_ratio_type;
  _ar_ratio_type ar_ratio;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _vector_base_to_rover_type;
  _vector_base_to_rover_type vector_base_to_rover;

   typedef float _distance_base_to_rover_type;
  _distance_base_to_rover_type distance_base_to_rover;

   typedef float _heading_base_to_rover_type;
  _heading_base_to_rover_type heading_base_to_rover;





  typedef boost::shared_ptr< ::inertial_sense::RTKRel_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::inertial_sense::RTKRel_<ContainerAllocator> const> ConstPtr;

}; // struct RTKRel_

typedef ::inertial_sense::RTKRel_<std::allocator<void> > RTKRel;

typedef boost::shared_ptr< ::inertial_sense::RTKRel > RTKRelPtr;
typedef boost::shared_ptr< ::inertial_sense::RTKRel const> RTKRelConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::inertial_sense::RTKRel_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::inertial_sense::RTKRel_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace inertial_sense

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'inertial_sense': ['/home/zyw/catkin_ws/src/isee_camvox/inertial-sense-ros/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::inertial_sense::RTKRel_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::inertial_sense::RTKRel_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::inertial_sense::RTKRel_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::inertial_sense::RTKRel_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::inertial_sense::RTKRel_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::inertial_sense::RTKRel_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::inertial_sense::RTKRel_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ff67521259c93bfc5ebd55747655bff6";
  }

  static const char* value(const ::inertial_sense::RTKRel_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xff67521259c93bfcULL;
  static const uint64_t static_value2 = 0x5ebd55747655bff6ULL;
};

template<class ContainerAllocator>
struct DataType< ::inertial_sense::RTKRel_<ContainerAllocator> >
{
  static const char* value()
  {
    return "inertial_sense/RTKRel";
  }

  static const char* value(const ::inertial_sense::RTKRel_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::inertial_sense::RTKRel_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
float32 differential_age 				# Age of differential (seconds)\n\
float32 ar_ratio 						# Ambiguity resolution ratio factor for validation\n\
geometry_msgs/Vector3 vector_base_to_rover 	# Vector to base (m) in ECEF - If Compassing enabled, this is the 3-vector from antenna 2 to antenna 1\n\
float32 distance_base_to_rover 				# Distance to Base (m)\n\
float32 heading_base_to_rover 				# Angle from north to vectorToBase in local tangent plane. (rad)\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::inertial_sense::RTKRel_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::inertial_sense::RTKRel_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.differential_age);
      stream.next(m.ar_ratio);
      stream.next(m.vector_base_to_rover);
      stream.next(m.distance_base_to_rover);
      stream.next(m.heading_base_to_rover);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RTKRel_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::inertial_sense::RTKRel_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::inertial_sense::RTKRel_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "differential_age: ";
    Printer<float>::stream(s, indent + "  ", v.differential_age);
    s << indent << "ar_ratio: ";
    Printer<float>::stream(s, indent + "  ", v.ar_ratio);
    s << indent << "vector_base_to_rover: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.vector_base_to_rover);
    s << indent << "distance_base_to_rover: ";
    Printer<float>::stream(s, indent + "  ", v.distance_base_to_rover);
    s << indent << "heading_base_to_rover: ";
    Printer<float>::stream(s, indent + "  ", v.heading_base_to_rover);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INERTIAL_SENSE_MESSAGE_RTKREL_H
