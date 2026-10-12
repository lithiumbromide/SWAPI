---
title: "InsertGlobalBoundingBox2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertGlobalBoundingBox2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGlobalBoundingBox2.html"
---

# InsertGlobalBoundingBox2 Method (IFeatureManager)

Inserts the specified global bounding box using a custom coordinate system. See [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) and [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGlobalBoundingBox2( _
   ByVal BBoxType As System.Integer, _
   ByVal lwtaDirectionType As System.Integer, _
   ByVal IncludeHiddenBodies As System.Boolean, _
   ByVal IncludeSurfaceBodies As System.Boolean, _
   ByRef Status As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BBoxType As System.Integer
Dim lwtaDirectionType As System.Integer
Dim IncludeHiddenBodies As System.Boolean
Dim IncludeSurfaceBodies As System.Boolean
Dim Status As System.Integer
Dim value As System.Object

value = instance.InsertGlobalBoundingBox2(BBoxType, lwtaDirectionType, IncludeHiddenBodies, IncludeSurfaceBodies, Status)
```

### C#

```csharp
System.object InsertGlobalBoundingBox2(
   System.int BBoxType,
   System.int lwtaDirectionType,
   System.bool IncludeHiddenBodies,
   System.bool IncludeSurfaceBodies,
   out System.int Status
)
```

### C++/CLI

```cpp
System.Object^ InsertGlobalBoundingBox2(
   System.int BBoxType,
   System.int lwtaDirectionType,
   System.bool IncludeHiddenBodies,
   System.bool IncludeSurfaceBodies,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BBoxType`: Bounding Box fit type as defined in [swGlobalBoundingBoxFitOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html) (see **Remarks**)
- `lwtaDirectionType`: Direction type as defined by [swGlobalBBoxLWTADirectionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBBoxLWTADirectionType_e.html)
- `IncludeHiddenBodies`: True to include hidden bodies, false to not
- `IncludeSurfaceBodies`: True to include surfaces, false to not
- `Status`: Status as defined by [swGlobalBoundingBoxResult_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxResult_e.html)

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertGlobalBoundingBox2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertGlobalBoundingBox2.html).

## Remarks

If BBoxType is set to swGlobalBoundingBoxFitOptions_e.swBoundingBoxType_CustomPlane, then select a face or plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) with TypeWanted set to [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES before calling this method.

To display or hide the Bounding Box sketch, call [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.html) to set [swUserPreferenceToggle_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swViewDispGlobalBBox to true or false, respectively.

After calling this method, use [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.html) to clear the selection made when the Bounding Box is created.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertGlobalBoundingBox Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGlobalBoundingBox.html)
[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
