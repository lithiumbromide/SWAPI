---
title: "SetReferences Method (ILibraryFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFeatureData"
member: "SetReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~SetReferences.html"
---

# SetReferences Method (ILibraryFeatureData)

Sets the references for the library feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferences( _
   ByVal RefVar As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFeatureData
Dim RefVar As System.Object

instance.SetReferences(RefVar)
```

### C#

```csharp
void SetReferences(
   System.object RefVar
)
```

### C++/CLI

```cpp
void SetReferences(
   System.Object^ RefVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RefVar`: Array of references

## VBA Syntax

See [LibraryFeatureData::SetReferences](ms-its:sldworksapivb6.chm::/sldworks~LibraryFeatureData~SetReferences.html).

## Examples

[Create Library Feature With References (C#)](Create_Library_Feature_With_References_Example_CSharp.htm)
[Create Library Feature With References (VB.NET)](Create_Library_Feature_With_References_Example_VBNET.htm)
[Create Library Feature With References (VBA)](Create_Library_Feature_With_References_Example_VB.htm)

## Remarks

Some SolidWorks properties and methods, such as this method, have an input object that must be marshaled to an IDispatch object array because System.Object has replaced VARIANT in the .NET framework. When marshaling System.Object to an IDispatch object array, you must explicitly control the marshaling behavior by using the System.Runtime.InteropServices.DispatchWrapper class. See the VB.NET and C# examples in this Help topic and [IDispatch Object Arrays as Input in .NET](sldworksAPIProgGuide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm) for more information.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)
[ILibraryFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html)
[ILibraryFeatureData::GetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferences.html)
[ILibraryFeatureData::GetReferencesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~GetReferencesCount.html)
[ILibraryFeatureData::IGetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~IGetReferences.html)
[ILibraryFeatureData::ISetReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData~ISetReferences.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
