---
title: "InsertGlobalBoundingBox Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertGlobalBoundingBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGlobalBoundingBox.html"
---

# InsertGlobalBoundingBox Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) and [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGlobalBoundingBox( _
   ByVal BBoxType As System.Integer, _
   ByVal IncludeHiddenBodies As System.Boolean, _
   ByVal IncludeSurfaceBodies As System.Boolean, _
   ByRef Status As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BBoxType As System.Integer
Dim IncludeHiddenBodies As System.Boolean
Dim IncludeSurfaceBodies As System.Boolean
Dim Status As System.Integer
Dim value As System.Object

value = instance.InsertGlobalBoundingBox(BBoxType, IncludeHiddenBodies, IncludeSurfaceBodies, Status)
```

### C#

```csharp
System.object InsertGlobalBoundingBox(
   System.int BBoxType,
   System.bool IncludeHiddenBodies,
   System.bool IncludeSurfaceBodies,
   out System.int Status
)
```

### C++/CLI

```cpp
System.Object^ InsertGlobalBoundingBox(
   System.int BBoxType,
   System.bool IncludeHiddenBodies,
   System.bool IncludeSurfaceBodies,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BBoxType`: Bounding Box fit type as defined in [swGlobalBoundingBoxFitOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html) (see **Remarks**)
- `IncludeHiddenBodies`: True to include hidden bodies, false to not
- `IncludeSurfaceBodies`: True to include surfaces, false to not
- `Status`: Status as defined by [swGlobalBoundingBoxResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxResult_e.html)

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertGlobalBoundingBox](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertGlobalBoundingBox.html).

## Examples

```
'VBA
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim longstatus As Long
Option Explicit
```

```
Sub main()

    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
```

```
    ' Display the Bounding Box sketch
    boolstatus = Part.SetUserPreferenceToggle)swViewDispGlobalBBox, True)

    Dim BoundingBox As SldWorks.Feature
    Set BoundingBox = Part.FeatureManager.InsertGlobalBoundingBox(swBoundingBoxType_BestFit, True, False, longstatus)
```

```
    Part.ClearSelection2 True
```

```
    ' Hide the Bounding Box sketch
    boolstatus = Part.SetUserPreferenceToggle)swViewDispGlobalBBox, False)
```

```
End Sub
```

## Remarks

If BBoxType is set to swGlobalBoundingBoxFitOptions_e.swBoundingBoxType_CustomPlane, then select a face or plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) with TypeWanted set to [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES before calling this method.

To display or hide the Bounding Box sketch, call [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) to set [swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swViewDispGlobalBBox to true or false, respectively.

After calling this method, use [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.html) to clear the selection made when the Bounding Box is created.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
