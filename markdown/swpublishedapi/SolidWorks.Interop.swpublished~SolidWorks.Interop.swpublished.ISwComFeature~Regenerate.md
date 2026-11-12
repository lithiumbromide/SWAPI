---
title: "Regenerate Method (ISwComFeature)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwComFeature"
member: "Regenerate"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature~Regenerate.html"
---

# Regenerate Method (ISwComFeature)

Allows you to rebuild a macro feature created using COM.

## Syntax

### Visual Basic (Declaration)

```vb
Function Regenerate( _
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

value = instance.Regenerate(app, modelDoc, feature)
```

### C#

```csharp
System.object Regenerate(
   System.object app,
   System.object modelDoc,
   System.object feature
)
```

### C++/CLI

```cpp
System.Object^ Regenerate(
   System.Object^ app,
   System.Object^ modelDoc,
   System.Object^ feature
)
```

### Parameters

- `app`: SOLIDWORKS application
- `modelDoc`: SOLIDWORKS document in which the macro appears
- `feature`: Macro feature that you want to rebuild

### Return Value

Any one of the following values:

- True if the rebuild is successful (independent and modify)
- False if the rebuild failed
- String, as displayed in an error message to the user (see **Remarks**)
- Body, if a body was created

## VBA Syntax

See [SwComFeature::Regenerate](ms-its:swpublishedapivb6.chm::/swpublished~SwComFeature~Regenerate.html).

## Remarks

This method is required.

Examples of string return values:

- VBA
  swmRebuild = "Macro feature output error message"
- C++ COM

  CComBSTR bMsg = _T("Macro feature output error message");
  _variant_t vBSTRRet = bMsg;
  *retval = vBSTRRet;
- C#

  functionReturnValue = "Macro feature output error message";
  return functionReturnValue;
- VB.NET

  Regenerate = "Macro feature output error message"

See [Exposed COM DLL or Executable and Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Exposed_COM_DLL_or_Executable.htm) and [Overview of Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

## See Also

[ISwComFeature Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature.html)
[ISwComFeature Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwComFeature_members.html)
[IMacroFeatureData Interface](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMacroFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
