---
title: "GetObjectId Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetObjectId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectId.html"
---

# GetObjectId Method (IModelDocExtension)

Gets the object ID for the specified annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetObjectId( _
   ByVal Annotation As Annotation _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Annotation As Annotation
Dim value As System.Integer

value = instance.GetObjectId(Annotation)
```

### C#

```csharp
System.int GetObjectId(
   Annotation Annotation
)
```

### C++/CLI

```cpp
System.int GetObjectId(
   Annotation^ Annotation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Annotation`: [Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

### Return Value

Object ID

## VBA Syntax

See [ModelDocExtension::GetObjectId](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetObjectId.html).

## Examples

[Get Object ID of GTol Annotation (C#)](Get_Object_ID_of_GTol_Annotation_Example_CSharp.htm)
[Get Object ID of GTol Annotation (VB.NET)](Get_Object_ID_of_GTol_Annotation_Example_VBNET.htm)
[Get Object ID of GTol Annotation (VBA)](Get_Object_ID_of_GTol_Annotation_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2014 SP5, Revision Number 22.5
