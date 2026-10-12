---
title: "ShowHelp Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowHelp"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowHelp.html"
---

# ShowHelp Method (ISldWorks)

Displays the specified Help topic.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowHelp( _
   ByVal HelpFile As System.String, _
   ByVal HelpTopic As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim HelpFile As System.String
Dim HelpTopic As System.Integer

instance.ShowHelp(HelpFile, HelpTopic)
```

### C#

```csharp
void ShowHelp(
   System.string HelpFile,
   System.int HelpTopic
)
```

### C++/CLI

```cpp
void ShowHelp(
   System.String^ HelpFile,
   System.int HelpTopic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HelpFile`: Name of the Help file that contains the Help topic
- `HelpTopic`: ID of Help topic to display

## VBA Syntax

See [SldWorks::ShowHelp](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowHelp.html).

## Examples

```vb
STDMETHODIMP CFuncFeatApp::appCallbackFunction(int cmd,int data,LPDISPATCH dsp, BOOL *retval)
{
            switch (cmd)
            {
            case     swAppIsNewCmd:
                        *retval = VARIANT_True; //Set to True if data is new
                        break;
            case     swAppWhatsNewDescription:
                            m_iSldWorks->ShowHelp(_T("name_of_your_Help_system.chm"), cmd);
                        break;
            case     swAppHelpContext:
                        break;
            }
            return S_OK;
}
```

## Examples

[Call Compiled HTML Help File (C#)](Call_Compiled_HTML_Help_File_Example_CSharp.htm)

## Remarks

You can use this method with [ISldWorks::AddCallback](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddCallback.html) to implement Interactive What's New for your add-in.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CallBack Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CallBack.html)
[ISldWorks::RemoveCallback Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveCallback.html)
[ISldWorks::SetAddinCallbackInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetAddinCallbackInfo.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
