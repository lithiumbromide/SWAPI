---
title: "SortCutList Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "SortCutList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SortCutList.html"
---

# SortCutList Method (IBodyFolder)

Sorts the cut list.

## Syntax

### Visual Basic (Declaration)

```vb
Function SortCutList( _
   ByVal CutListSortOptions As System.Object, _
   ByVal IgnoreInvalidFacesOrFeatures As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim CutListSortOptions As System.Object
Dim IgnoreInvalidFacesOrFeatures As System.Boolean
Dim value As System.Boolean

value = instance.SortCutList(CutListSortOptions, IgnoreInvalidFacesOrFeatures)
```

### C#

```csharp
System.bool SortCutList(
   System.object CutListSortOptions,
   System.bool IgnoreInvalidFacesOrFeatures
)
```

### C++/CLI

```cpp
System.bool SortCutList(
   System.Object^ CutListSortOptions,
   System.bool IgnoreInvalidFacesOrFeatures
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CutListSortOptions`: [ICutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.html)
- `IgnoreInvalidFacesOrFeatures`: True to sort bodies ignoring any invalid excluded faces/features, false to not sort the bodies if there are invalid excluded faces/features (see **Remarks**)

### Return Value

True if sorting is successful, false if not

## VBA Syntax

See ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetBodyCount.html[BodyFolder::SortCutList](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~SortCutList.html).

## Examples

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html) examples.

## Remarks

Use [IBodyFolder::GetCutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListSortOptions.html) to populate CutListSortOptions.

This method applies the CutListSortOptions settings, sorts the cut list, and refreshes the cut list in the FeatureManager design tree.

In the Cut List Sorting Options PropertyManager you select faces/features to exclude from sorting. If some of those selected faces/features to exclude are invalid, i.e., they are not of selection type BODYFEATURE or FACE or they cannot be excluded (see the end of this **Remark**), a dialog box pops up during the sort operation with:

----------------------------------------------------------------------

**Failed to exclude some of the selected faces in cut list sorting. Try selecting the corresponding features instead.**

**Would you like to continue:**

**Yes (Bodies will be sorted ignoring some of the excluded faces.)**

**No (Bodies will not be sorted.)**

**----------------------------------------------------------**

IgnoreInvalidFacesOrFeatures handles the situation when some of the body faces/features selected for exclusion ([ICutListSortOptions::SetFacesOrFeaturesToExclude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~SetFacesOrFeaturesToExclude.html)) can not be excluded.

Set IgnoreInvalidFacesOrFeatures to:

- True, to sort bodies ignoring any invalid excluded faces/features.
- False, to not sort the bodies if there are invalid excluded faces/features.

If you set IgnoreInvalidFacesOrFeatures to false and there are invalid faces/features in the exclusion list, then this method will not sort the cut list.

Other examples of faces and features that are invalid for exclusion:

- Chamfers that remove an entire face.
- Suppressed features.
- Features that create new bodies from sketches, such as boss-extrude, revolve, and sweep.
- Certain sheet metal features.

For more information, see the **Sorting Cut Lists** topics in the SOLIDWORKS Design user-interface help.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
