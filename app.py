import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(
        page_title="Chat Assistant",
        page_icon="💬",
        layout="wide"
    )

    st.title("Chat Assistant")

    # Voiceflow chat widget HTML
    voiceflow_html = """
    <div style="height: 600px;">
        <script type="text/javascript">
            (function(d, t) {
                var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
                v.onload = function() {
                    window.voiceflow.chat.load({
                        verify: { projectID: '67780033ae2ed1739d0b87bb' },
                        url: 'https://general-runtime.voiceflow.com',
                        versionID: 'production'
                    });
                }
                v.src = "https://cdn.voiceflow.com/widget/bundle.mjs";
                v.type = "text/javascript";
                s.parentNode.insertBefore(v, s);
            })(document, 'script');
        </script>
    </div>
    """

    # Inject the HTML using streamlit components
    components.html(voiceflow_html, height=650)

if __name__ == "__main__":
    main()