---
title: "GetAttributes Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetAttributes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.html"
---

# GetAttributes Method (ISketchBlockInstance)

Gets the attributes for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttributes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim value As System.Object

value = instance.GetAttributes()
```

### C#

```csharp
System.object GetAttributes()
```

### C++/CLI

```cpp
System.Object^ GetAttributes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of attributes (see **Remarks**)

## VBA Syntax

See [SketchBlockInstance::GetAttributes](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetAttributes.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

## Remarks

Attributes are string notes that have tag names and are not read-only.

Use [ISketchBlockInstance::GetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html) to get attribute's value, or use [ISketchBlockInstance::SetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html) to set an attribute's value.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetAttributeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.html)
[ISketchBlockInstance::IGetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
