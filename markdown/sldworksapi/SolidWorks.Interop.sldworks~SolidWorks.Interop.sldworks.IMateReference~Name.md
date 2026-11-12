---
title: "Name Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~Name.html"
---

# Name Property (IMateReference)

Gets the name of the selected mate reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
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

Name of the selected mate reference

## VBA Syntax

See [MateReference::Name](ms-its:sldworksapivb6.chm::/sldworks~MateReference~Name.html).

## Examples

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

## See Also

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
