---
title: "Long vs. Integer"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Long_vs_Integer.htm"
---

# Long vs. Integer

The programming language and the version of SOLIDWORKS (32-bit or 64-bit) determine whether longs or integers are passed to or returned by parameters that expect or return these data types.

##### SOLIDWORKS (32-bit)

| Programming Language | 16-bit Data Type | 32-bit Data Type | 64-bit Data Type |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| C# |  |  | int | Int32 | long | Int64 |
|  |  |  |  |  |  |  |
| Managed C++ |  |  | long | Int32 | LONGLONG (=__int64) | Int64 |
|  |  |  | int | Int32 |  |  |
| Unmanaged C++ |  |  | long | N/A | LONGLONG (=__int64) | N/A |
|  |  |  | int | N/A |  |  |
| VBA | Integer | N/A | Long | N/A |  |  |
|  |  |  | LongPtr | N/A |  |  |
| VB.NET |  |  | Integer | Int32 | Long | Int64 |

##### SOLIDWORKS x64 (64-bit)

| Programming Language | 16-bit Data Type | 32-bit Data Type | 64-bit Data Type |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| C# |  |  | int | Int32 | long | Int64 |
|  |  |  |  |  |  |  |
| Managed C++ |  |  | long | Int32 | LONGLONG (=__int64) | I nt64 |
|  |  |  | int | Int32 |  |  |
| Unmanaged C++ |  |  | long | N/A | LONGLONG (=__int64) | N/A |
|  |  |  | int | N/A |  |  |
| VBA | Integer | N/A | Long | N/A | LongLong | N/A |
|  |  |  |  |  | LongPtr | N/A |
| VB.NET |  |  | Integer | Int32 | Long | Int64 |

In the previous tables, Int32 and Int64 indicate the .NET equivalents. Incorrectly casting a variable results in a runtime error.

See [VBA and SOLIDWORKS x64](VBA_and_SolidWorks_x64.htm) for more information about the LongPtr variable type and VBA.
