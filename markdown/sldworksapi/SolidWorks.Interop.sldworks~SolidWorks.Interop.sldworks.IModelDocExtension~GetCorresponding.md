---
title: "GetCorresponding Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCorresponding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.html"
---

# GetCorresponding Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::GetCorresponding2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorresponding( _
   ByVal InputObject As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim InputObject As System.Object
Dim value As System.Object

value = instance.GetCorresponding(InputObject)
```

### C#

```csharp
System.object GetCorresponding(
   System.object InputObject
)
```

### C++/CLI

```cpp
System.Object^ GetCorresponding(
   System.Object^ InputObject
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InputObject`: Pointer to the Dispatch object in the assembly context

### Return Value

Pointer to the corresponding object in the underlying part, assembly, or subassembly document

## VBA Syntax

See [ModelDocExtension::GetCorresponding](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCorresponding.html).

## Examples

[Get Corresponding Note in Assembly (VBA)](Get_Corresponding_Note_in_Assembly_Example_VB.htm)
[Get Corresponding Note in Part (VBA)](Get_Corresponding_Note_in_Part_Example_VB.htm)

## Remarks

Given an object in an assembly context, this method gets the corresponding object in the underlying component document regardless of whether the document is a part or an assembly.

You can use this method with any object assigned a persistent reference ID; for example, a [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) or [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) object.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)
[IComponent2::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.html)
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html)
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15.1
