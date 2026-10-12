---
title: "Name Property (ISnapShot)"
project: "SOLIDWORKS API Help"
interface: "ISnapShot"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot~Name.html"
---

# Name Property (ISnapShot)

Gets or sets the name of this snapshot.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISnapShot
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- Name of the snapshot

- or -

- "" to give a default name of "Snap`n`"

- or -

- "?" to open the Name Snapshot dialog box

## VBA Syntax

See [SnapShot::Name](ms-its:sldworksapivb6.chm::/sldworks~SnapShot~Name.html).

## Examples

[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)

## See Also

[ISnapShot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot.html)
[ISnapShot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
