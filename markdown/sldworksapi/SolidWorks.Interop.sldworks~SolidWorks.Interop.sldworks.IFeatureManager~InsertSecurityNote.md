---
title: "InsertSecurityNote Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSecurityNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSecurityNote.html"
---

# InsertSecurityNote Method (IFeatureManager)

Inserts a note for the specified [macro feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSecurityNote( _
   ByVal Text As System.String, _
   ByVal FeatureOwner As Feature _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Text As System.String
Dim FeatureOwner As Feature
Dim value As Note

value = instance.InsertSecurityNote(Text, FeatureOwner)
```

### C#

```csharp
Note InsertSecurityNote(
   System.string Text,
   Feature FeatureOwner
)
```

### C++/CLI

```cpp
Note^ InsertSecurityNote(
   System.String^ Text,
   Feature^ FeatureOwner
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Text for note
- `FeatureOwner`: Macro feature for this note

### Return Value

Point to [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) object

## VBA Syntax

See [FeatureManager::InsertSecurityNote](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSecurityNote.html).

## Remarks

The note is for display purposes only and cannot be modified by the end user. For example, you could display the note to inform an end user that editing or deleting the macro feature is prohibited.

You associate the note with the specified macro feature in:

- VB by using this method in the code that generates the macro feature and by setting swMacroFeatureSecurityEnableNote in the [macro feature's security function](sldworksAPIProgGuide.chm::/Macro_Features/Security_Function.htm). You should also include the conditions under which to display the note.
- C++ by using this method in the code that generates the macro feature and by setting swMacroFeatureSecurityEnableNote for the Options argument of [ISwComFeature::Security](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwComFeature~Security.html) in the [macro feature's security function](sldworksAPIProgGuide.chm::/Macro_Features/Security_Function.htm). You should also include the conditions under which to display the note.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
