---
title: "Edit Method (ISwComFeature)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwComFeature"
member: "Edit"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature~Edit.html"
---

# Edit Method (ISwComFeature)

Allows you to edit the definition of a macro feature created using COM.

## Syntax

### Visual Basic (Declaration)

```vb
Function Edit( _
   ByVal app As System.Object, _
   ByVal modelDoc As System.Object, _
   ByVal feature As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwComFeature
Dim app As System.Object
Dim modelDoc As System.Object
Dim feature As System.Object
Dim value As System.Object

value = instance.Edit(app, modelDoc, feature)
```

### C#

```csharp
System.object Edit(
   System.object app,
   System.object modelDoc,
   System.object feature
)
```

### C++/CLI

```cpp
System.Object^ Edit(
   System.Object^ app,
   System.Object^ modelDoc,
   System.Object^ feature
)
```

### Parameters

- `app`: SOLIDWORKS application
- `modelDoc`: SOLIDWORKS document in which the macro feature appears
- `feature`: Macro feature whose definition you want to edit

### Return Value

True if editing the definition of the macro feature is successful, false if not

## VBA Syntax

See [SwComFeature::Edit](ms-its:swpublishedapivb6.chm::/swpublished~SwComFeature~Edit.html).

## Remarks

This method is required. See [Exposed COM DLL or Executable and Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Exposed_COM_DLL_or_Executable.htm) and [Overview of Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

## See Also

[ISwComFeature Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature.html)
[ISwComFeature Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature_members.html)
[IFeatureManager::InsertSecurityNote Method](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSecurityNote.html)
[IMacroFeatureData Interface](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
