---
title: "Comment Property (ISnapShot)"
project: "SOLIDWORKS API Help"
interface: "ISnapShot"
member: "Comment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot~Comment.html"
---

# Comment Property (ISnapShot)

Gets or sets the comment on this snapshot.

## Syntax

### Visual Basic (Declaration)

```vb
Property Comment As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISnapShot
Dim value As System.String

instance.Comment = value

value = instance.Comment
```

### C#

```csharp
System.string Comment {get; set;}
```

### C++/CLI

```cpp
property System.String^ Comment {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Comment (see **Remarks**)

## VBA Syntax

See [SnapShot::Comment](ms-its:sldworksapivb6.chm::/sldworks~SnapShot~Comment.html).

## Examples

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

## Remarks

To add a time stamp to the comment, prepend the comment string with "<TS>".

For example:

snap1.Comment = "<TS> This is a comment for SnapShot1"

generates:

07/29/2011 04:08 PM `user_id`: This is a comment for SnapShot1

## See Also

[ISnapShot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.html)
[ISnapShot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
