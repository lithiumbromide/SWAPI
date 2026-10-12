---
title: "GetAttributeValue Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "GetAttributeValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html"
---

# GetAttributeValue Method (ISketchBlockInstance)

Gets the value of the specified attribute for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttributeValue( _
   ByVal TagName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim TagName As System.String
Dim value As System.String

value = instance.GetAttributeValue(TagName)
```

### C#

```csharp
System.string GetAttributeValue(
   System.string TagName
)
```

### C++/CLI

```cpp
System.String^ GetAttributeValue(
   System.String^ TagName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TagName`: Tag name of this attribute

### Return Value

Value of this attribute

## VBA Syntax

See [SketchBlockInstance::GetAttributeValue](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~GetAttributeValue.html).

## Remarks

Attributes are notes that have tag names and are not read-only.

Use [ISketchBlockInstance::SetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html) to set an attribute.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetAttributeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.html)
[ISketchBlockInstance::GetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.html)
[ISketchBlockInstance::IGetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
