import streamlit as st
import json
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Internship Scout",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Dark theme + orange accent styles ─────────────────────────────────────────
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background: linear-gradient(
            180deg,
            #2D3748 0%,
            #1A202C 100%
        );
        color: #FFFFFF !important;
    }

    [data-testid="stHeader"] { background-color: #0e0e0e; }
    [data-testid="stSidebar"] { background-color: #141414; }

    /* Hero headline */
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(90deg, #ff6b1a 0%, #ffaa55 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.1rem;
    }
    .hero-sub {
        font-size: 1rem;
        color: #4b5563;
        font-weight: 500;
        margin-bottom: 2rem;
    }

    /* Section labels */
    .section-label {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #ff6b1a;
        margin-bottom: 0.4rem;
    }

    /* Select boxes / inputs */
    div[data-baseweb="select"] > div {
        background-color: white !important;
        border: 1px solid #d1d5db !important;
        border-radius: 8px !important;
        color: #111827 !important;
    }
    div[data-baseweb="select"] svg { color: #ff6b1a !important; }

    /* Primary button */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b1a 0%, #e85d10 100%);
        color: #fff;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1rem;
        padding: 0.6rem 2rem;
        width: 100%;
        transition: opacity 0.15s;
        letter-spacing: 0.02em;
    }
    .stButton > button:hover { opacity: 0.88; }

    /* Metric cards */

    [data-testid="metric-container"] {
        background: #374151;
        border: 1px solid #E5E7EB;
        border-radius: 14px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    [data-testid="metric-container"] label {
        color: #374151 !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #1f2937 !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
    }

    /* Internship card */
    .card {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 14px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .card:hover { border-color: #ff6b1a; }
    .card-company {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #ff6b1a;
        margin-bottom: 0.2rem;
    }
    .card-role {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.4rem;
    }
    .card-meta {
        font-size: 0.82rem;
        color: #777;
        margin-bottom: 0.8rem;
    }
    .card-score {
        display: inline-block;
        background: #1f1200;
        color: #ff9044;
        border: 1px solid #ff6b1a44;
        border-radius: 6px;
        padding: 0.18rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        margin-right: 0.5rem;
    }
    .apply-btn {
        display: inline-block;
        background: linear-gradient(135deg, #ff6b1a, #e85d10);
        color: #fff !important;
        text-decoration: none;
        border-radius: 6px;
        padding: 0.25rem 1rem;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.03em;
    }
    .apply-btn:hover { opacity: 0.85; text-decoration: none; }

    /* Divider */
    hr { border-color: #222; }

    /* Download button */
    [data-testid="stDownloadButton"] > button {
        background: #1a1a1a;
        color: #ff6b1a;
        border: 1px solid #ff6b1a55;
        border-radius: 8px;
        font-weight: 600;
    }
    [data-testid="stDownloadButton"] > button:hover {
        background: #ff6b1a22;
    }

    /* Status / spinner text */
    .stSpinner > div { color: #ff6b1a !important; }
    [data-testid="stStatusWidget"] { color: #ff6b1a; }

    /* Alert boxes */
    [data-testid="stAlert"] {
        background: #1a1100;
        border-left: 3px solid #ff6b1a;
        color: #e8e8e8;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Lazy imports (backend) ────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def _import_backends():
    from search_linkedin import search_linkedin
    from filter_agent import filter_internships
    from verification_agent import verify_internship
    from ranking_agent import rank_internships
    from location_filter_agent import filter_by_location
    from save_results import save_results
    from compare_results import find_new_internships
    from email_agent import send_email
    return (
        search_linkedin,
        filter_internships,
        verify_internship,
        rank_internships,
        filter_by_location,
        save_results,
        find_new_internships,
        send_email,
    )

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">AI Internship Scout</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Automated search · AI verification · Smart ranking</div>',
    unsafe_allow_html=True,
)

# ── Controls ──────────────────────────────────────────────────────────────────
INTERNSHIP_TYPES = [
    "All",
    "AI",
    "Machine Learning",
    "Data Science",
    "Software Development",
    "Web Development",
    "Cloud Computing",
    "DevOps",
    "Cybersecurity",
    "Embedded Systems",
    "IoT",
]

REGIONS = [
    "All",
    "India",
    "USA",
    "Europe",
    "Singapore",
    "Malaysia",
    "Australia",
    "NewZealand",
    "China",
]

RESULT_COUNTS = [10, 25, 50]

col1, col2, col3, col4 = st.columns([3, 2, 1.5, 1.5])
with col1:
    st.markdown('<div class="section-label">Internship Type</div>', unsafe_allow_html=True)
    internship_type = st.selectbox(
        "Internship Type",
        INTERNSHIP_TYPES,
        label_visibility="collapsed",
    )
with col2:
    st.markdown('<div class="section-label">Region</div>', unsafe_allow_html=True)
    region = st.selectbox(
        "Region",
        REGIONS,
        label_visibility="collapsed",
    )
with col3:
    st.markdown('<div class="section-label">Results</div>', unsafe_allow_html=True)
    top_count = st.selectbox(
        "Results",
        RESULT_COUNTS,
        label_visibility="collapsed",
    )
with col4:
    st.markdown('<div class="section-label">&nbsp;</div>', unsafe_allow_html=True)
    search_clicked = st.button("🔍 Search", use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "results" not in st.session_state:
    st.session_state.results = None
if "metrics" not in st.session_state:
    st.session_state.metrics = None

# ── Search workflow ───────────────────────────────────────────────────────────
if search_clicked:

    start_time = time.time()

    try:
        (
            search_linkedin,
            filter_internships,
            verify_internship,
            rank_internships,
            filter_by_location,
            save_results,
            find_new_internships,
            send_email,
        ) = _import_backends()
    except Exception as import_err:
        st.error(f"Backend import failed: {import_err}")
        st.stop()

    location_mode = region.lower() if region != "All" else "all"

    # ── Step 1: Search ────────────────────────────────────────────────────────
    if internship_type == "All":
        keywords = [
            "ai",
            "machine learning",
            "data science",
            "software engineer",
            "python",
            "web development",
            "cloud",
            "devops",
            "cybersecurity",
            "electronics",
            "embedded systems",
            "iot",
        ]
        raw_results = []
        with st.spinner("Searching internships across all categories…"):
            for kw in keywords:
                jobs = search_linkedin(kw, location_mode)
                raw_results.extend(jobs)
        # Deduplicate by link
        unique_jobs = {}
        for job in raw_results:
            link = job.get("link", "")
            if link:
                unique_jobs[link] = job
        raw_results = list(unique_jobs.values())
    else:
        keyword = internship_type.lower()
        with st.spinner(f"Searching {internship_type} internships…"):
            raw_results = search_linkedin(keyword, location_mode)
    total_found = len(raw_results)

    # ── Step 2: Filter ────────────────────────────────────────────────────────
    with st.spinner("Filtering internships…"):
        filtered = filter_internships(raw_results)
    after_filter = len(filtered)

    # ── Step 3: Verify ────────────────────────────────────────────────────────
    verified_results = []
    progress_bar = st.progress(0, text="Verifying internships…")
    for idx, internship in enumerate(filtered):
        score = verify_internship(internship)
        if score >= 50:
            internship["score"] = score
            verified_results.append(internship)
        progress_bar.progress(
            (idx + 1) / max(len(filtered), 1),
            text=f"Verifying internships… {idx + 1}/{len(filtered)}",
        )
    progress_bar.empty()
    verified_count = len(verified_results)

    # ── Step 4: Rank ──────────────────────────────────────────────────────────
    with st.spinner("Ranking internships…"):
        top_internships = rank_internships(verified_results, top_count)

    # ── Step 5: Filter by location ────────────────────────────────────────────
    with st.spinner("Filtering by location…"):
        top_internships = filter_by_location(top_internships, location_mode)
    ranked_count = len(top_internships)
        
    # ── Step 6: Compare ───────────────────────────────────────────────────────
    with st.spinner("Comparing with previous results…"):
        new_internships = find_new_internships(top_internships)

    # ── Step 7: Save Results ───────────────────────────────────────────────────────
    with st.spinner("Saving results…"):
        save_results(top_internships)
   
        st.info(f"🆕 New Internships Found: {len(new_internships)}")

        
    # ── Step 8: Email ─────────────────────────────────────────────────────────
    with st.spinner("Sending email digest…"):
        try:
            send_email(new_internships)
        except Exception as e:
            st.warning(f"Email skipped: {e}")        

    end_time = time.time()

    search_time = round(
        end_time - start_time,
        2
    )

    if len(new_internships) > 0:
        st.session_state.results = new_internships
    else:
        st.session_state.results = []

    highest_score = 0

    if top_internships:

        highest_score = max(
            internship.get(
                "final_score",
                0
            )

            for internship in top_internships
       )

    st.session_state.metrics = {
        "total_found": total_found,
        "after_filter": after_filter,
        "verified": verified_count,
        "ranked": ranked_count,
        "new_internships": len(new_internships),
        "search_time": search_time,
        "highest_score": highest_score,
    }

# ── Display results ───────────────────────────────────────────────────────────
if st.session_state.metrics:
    m = st.session_state.metrics
    st.markdown('<div class="section-label">Run Summary</div>', unsafe_allow_html=True)
    mc1, mc2, mc3, mc4, mc5, mc6, mc7  = st.columns(7)
    mc1.metric("Total Found", m["total_found"])
    mc2.metric("After Filter", m["after_filter"])
    mc3.metric("Verified", m["verified"])
    mc4.metric("Ranked", m["ranked"])
    mc5.metric("New Internships", m["new_internships"])
    mc6.metric("Time (s)", m["search_time"])
    mc7.metric("Top Score",m["highest_score"])
    
    st.markdown("<hr>", unsafe_allow_html=True)


if st.session_state.results:
    results = st.session_state.results

    top_row_left, top_row_right = st.columns([6, 2])
    with top_row_left:
        st.markdown(
            f'<div class="section-label">{len(results)} Internship{"s" if len(results) != 1 else ""} Found</div>',
            unsafe_allow_html=True,
        )
    with top_row_right:
        st.download_button(
            label="⬇ Download JSON",
            data=json.dumps(results, indent=2, ensure_ascii=False),
            file_name="internships.json",
            mime="application/json",
            use_container_width=True,
        )

    for internship in results:
        company  = internship.get("company", "Unknown Company")
        role     = internship.get("role", "Internship")
        location = internship.get("location", "—")
        link     = internship.get("link", "#")
        score    = internship.get("final_score") or internship.get("score") or 0

        apply_html = (
            f'<a class="apply-btn" href="{link}" target="_blank" rel="noopener">Apply Now ↗</a>'
            if link and link != "#"
            else '<span style="color:#555;font-size:0.8rem;">No link available</span>'
        )

        card_html = f"""
        <div class="card">
            <div class="card-company">{company}</div>
            <div class="card-role">{role}</div>
            <div class="card-meta">📍 {location}</div>
            <span class="card-score">Score: {score}</span>
            {apply_html}
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

elif not search_clicked:
    st.markdown(
        """
        <div style="text-align:center; padding: 4rem 0; color: #444;">
            <div style="font-size:3rem; margin-bottom:1rem;">🔍</div>
            <div style="font-size:1rem;">Select your filters above and click <strong style="color:#ff6b1a;">Search</strong> to discover internships.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
