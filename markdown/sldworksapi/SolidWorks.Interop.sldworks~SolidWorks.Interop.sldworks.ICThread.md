---
title: "ICThread Interface"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html"
---

# ICThread Interface

Allows access to a cosmetic thread.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICThread
```

### Visual Basic (Usage)

```vb
Dim instance As ICThread
```

### C#

```csharp
public interface ICThread
```

### C++/CLI

```cpp
public interface class ICThread
```

## VBA Syntax

See [CThread](ms-its:sldworksapivb6.chm::/sldworks~CThread.html).

## Examples

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## Remarks

A cosmetic thread annotation in a drawing is typically associated with a cosmetic thread feature in the underlying model. The name of the annotation is the same as the name of the feature.

Use:

1. [IAnnotation::GetName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetName.html) to get the name of the CThread annotation in the drawing.
2. [IPartDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FeatureByName.html) or [IPartDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IFeatureByName.html) with that name, to get that feature in the model.
3. [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) to access the cosmetic thread model data once you have the feature.

## Accessors

[IAnnotation::GetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetSpecificAnnotation.html) or [IAnnotation::IGetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html)

[ICThread::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~GetNext.html) and [ICThread::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~IGetNext.html)

[IView::GetFirstCThread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstCThread.html) and [IView::IGetFirstCThread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetFirstCThread.html)

[IView::GetCThreads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCThreads.html) and [IView::IGetCThreads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetCThreads.html)

## Access Diagram

[CThread](SWObjectModel.pdf#CThread)

## See Also

[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::HasLegacyCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads.html)
