---
title: "IGetAttributes Method (ISketchBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockInstance"
member: "IGetAttributes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.html"
---

# IGetAttributes Method (ISketchBlockInstance)

Gets the attributes for this block instance.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAttributes( _
   ByVal Count As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockInstance
Dim Count As System.Integer
Dim value As Note

value = instance.IGetAttributes(Count)
```

### C#

```csharp
Note IGetAttributes(
   System.int Count
)
```

### C++/CLI

```cpp
Note^ IGetAttributes(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of attributes

### Return Value

- in-process, unmanaged C++: Pointer to an array of [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Attributes are notes that have tag names and are not read-only.

Before calling this method, call [ISketchBlockInstance::GetAttributeCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.html) to get the value for Count.

Use [ISketchBlockInstance::GetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html) to get attribute's value, or use [ISketchBlockInstance::SetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html) to set an attribute's value.

## See Also

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.html)
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html)
[ISketchBlockInstance::GetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.html)
[ISketchBlockInstance::GetAttributeValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html)
[ISketchBlockInstance::SetAttributeValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
