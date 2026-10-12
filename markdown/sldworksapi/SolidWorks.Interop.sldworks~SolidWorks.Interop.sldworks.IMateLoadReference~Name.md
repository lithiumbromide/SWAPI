---
title: "Name Property (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Name.html"
---

# Name Property (IMateLoadReference)

Gets the name of this mate load reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim value As System.String

value = instance.Name
```

### C#

```csharp
System.string Name {get;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of mate load reference

## VBA Syntax

See [MateLoadReference::Name](ms-its:sldworksapivb6.chm::/sldworks~MateLoadReference~Name.html).

## Examples

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
