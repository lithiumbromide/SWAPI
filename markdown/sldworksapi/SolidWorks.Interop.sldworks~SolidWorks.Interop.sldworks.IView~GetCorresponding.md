---
title: "GetCorresponding Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCorresponding"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorresponding.html"
---

# GetCorresponding Method (IView)

Gets the object in this drawing view that corresponds to the specified part or assembly object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorresponding( _
   ByVal InputObject As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
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

- `InputObject`: Pointer to the Dispatch object in a part or assembly (see **Remarks**)

### Return Value

Pointer to the corresponding object in this drawing view; null or Nothing if none found

## VBA Syntax

See [View::GetCorresponding](ms-its:sldworksapivb6.chm::/sldworks~View~GetCorresponding.html).

## Examples

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

## Remarks

InputObject can be any object assigned a persistent reference or object ID; for example, [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html), [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html), [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html), [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html), etc.

Annotation objects will be found only if they were previously imported into this drawing view.

Use [IModelDocExtension::GetCorresponding2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2.html) to get the part or assembly object that corresponds to an object in a drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCorrespondingEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
