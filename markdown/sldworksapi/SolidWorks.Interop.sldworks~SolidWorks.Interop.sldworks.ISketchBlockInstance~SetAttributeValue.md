---
title: "SetAttributeValue Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "SetAttributeValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html"
---

# SetAttributeValue Method (ISketchBlockInstance)

Sets the value of the specified attribute for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAttributeValue( _
   ByVal TagName As System.String, _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim TagName As System.String
Dim Value As System.String
Dim value As System.Boolean

value = instance.SetAttributeValue(TagName, Value)
```

### C#

```csharp
System.bool SetAttributeValue(
   System.string TagName,
   System.string Value
)
```

### C++/CLI

```cpp
System.bool SetAttributeValue(
   System.String^ TagName,
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TagName`: Tag name of this attribute
- `Value`: Value for this attribute

### Return Value

True if the attribute's value is set, false if not

## VBA Syntax

See [SketchBlockInstance::SetAttributeValue](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockInstance~SetAttributeValue.html).

## Remarks

Attributes are string notes that have tag names and are not read-only.

Use [ISketchBlockInstance::GetAttributes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributes.html) or [ISketchBlockInstance::IGetAttributes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html) to the get attributes for this block instance. Use [ISketchBlockInstance::GetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html) to get an attribute's value.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
