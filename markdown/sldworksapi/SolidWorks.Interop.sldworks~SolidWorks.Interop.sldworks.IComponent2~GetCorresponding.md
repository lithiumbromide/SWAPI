---
title: "GetCorresponding Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetCorresponding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorresponding.html"
---

# GetCorresponding Method (IComponent2)

Gets the corresponding object in the context of the assembly for a specific instance of the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorresponding( _
   ByVal InputObject As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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

- `InputObject`: Pointer to the Dispatch object

### Return Value

Pointer to the corresponding object in the context of the assembly for an instance of the component

## VBA Syntax

See [Component2::GetCorresponding](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetCorresponding.html).

## Examples

[Get Corresponding Objects in Assembly Component (C#)](Get_Corresponding_Objects_in_Assembly_Component_Example_CSharp.htm)
[Get Corresponding Objects in Assembly Component (VB.NET)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)
[Get Corresponding Objects in Assembly Component (VBA)](Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm)

## Remarks

Given an object in an underlying component document, this method gets the corresponding object in the context of the assembly for a specific instance of that component document (i.e., there can be more than one instance).

You can use this method with any object assigned a persistent reference or object ID; for example, [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html), [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html), [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html), etc.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html)
[IComponent2::IGetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetCorrespondingEntity.html)
[IModelDocExtension::GetCorresponding Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding.html)
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
