---
title: "GetAllCustomPropertiesCount Method (IWeldmentCutListAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListAnnotation"
member: "GetAllCustomPropertiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomPropertiesCount.html"
---

# GetAllCustomPropertiesCount Method (IWeldmentCutListAnnotation)

Gets the number of items in the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllCustomPropertiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListAnnotation
Dim value As System.Integer

value = instance.GetAllCustomPropertiesCount()
```

### C#

```csharp
System.int GetAllCustomPropertiesCount()
```

### C++/CLI

```cpp
System.int GetAllCustomPropertiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of available custom properties

## VBA Syntax

See [WeldmentCutListAnnotation::GetAllCustomPropertiesCount](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListAnnotation~GetAllCustomPropertiesCount.html).

## Examples

[Get Weldment Cut List Feature and Annotations (VBA)](Get_Weldment_Cut-list_Feature_and_Annotations_Example_VB.htm)
[Get Weldment Cut List Feature and Annotations (VB.NET)](Get_Weldment_Cut-list_Feature_and_Annotations_Example_VBNET.htm)
[Get Weldment Cut List Feature and Annotations (C#)](Get_Weldment_Cut-list_Feature_and_Annotations_Example_CSharp.htm)

## Remarks

Call this method before calling [IWeldmentCutListAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties.html).

The list of possible custom properties includes all of the items in the weldment cut list table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.html)
[IWeldmentCutListAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.html)
[IWeldmentCutListAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty.html)
[IWeldmentCutListAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
